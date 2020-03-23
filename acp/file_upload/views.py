from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document, Emotion
from django.db.models.signals import post_save, pre_save


import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics import confusion_matrix

import csv
from django.conf import settings


def model_form_upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DocumentForm()

    return render(
        request, "file_upload/upload.html", {"form": form, "title": "Upload File",}
    )


def file_upload(sender, instance, **kwargs):
    from sklearn import svm

    instance = instance.document
    root = settings.MEDIA_ROOT
    file_loc = f"{root}/{instance}"
    print(file_loc)
    print(root)
    data = pd.read_csv(
        "C:/Users/Ardy/Desktop/acp\media/documents/xps_edited.csv", encoding="latin-1"
    )
    test_data = pd.read_csv(file_loc, encoding="latin-1")
    happy = 0
    panic = 0
    frustrated = 0
    bored = 0

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
        data["keystrokes"], data["emotion"], test_size=0.1, random_state=1
    )

    # # training vectorizer
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train)

    # training the classifier
    svm = svm.SVC(C=1000)
    svm.fit(X_train, y_train)

    test = test_data["keystrokes"]

    # testing against testing set
    X_test = vectorizer.transform(test)
    y_pred = svm.predict(X_test)
    # print(confusion_matrix(y_test, y_pred))
    # print(y_pred)

    for y in y_pred:

        if y == "Happy":
            happy += 1
        elif y == "Panic":
            panic += 1
        elif y == "Bored":
            bored += 1
        elif y == "Frustrated":
            frustrated += 1
        else:
            print("Error in your code!")

    emotion = Emotion.objects.get(id=1,)
    emotion.happy = happy
    emotion.panic = panic
    emotion.bored = bored
    emotion.frustrated = frustrated
    emotion.save()

    # print(happy, panic, frustrated, bored)
    # context = {"happy": happy, "panic": panic, "bored": bored, "frustrated": frustrated}


post_save.connect(file_upload, Document)
