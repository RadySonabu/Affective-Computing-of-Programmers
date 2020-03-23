from django.shortcuts import render
from django.http import HttpResponse
from .resources import Documents
from file_upload.models import Emotion


def download(request):
    emotion = Emotion.objects.all()

    for e in emotion:
        happy = e.happy
        panic = e.panic
        bored = e.bored
        frustrated = e.frustrated

    if happy > panic and happy > bored and happy > frustrated:
        emotion_1 = "Happy"
        color = "orange"
    elif panic > bored and panic > frustrated:
        emotion_1 = "Panic"
        color = "violet"
    elif bored > frustrated:
        emotion_1 = "Bored"
        color = "gray"
    else:
        emotion_1 = "Frustrated"
        color = "red"

    return render(
        request,
        "file_download/download.html",
        {
            "title": "Download File",
            "happy": happy,
            "panic": panic,
            "bored": bored,
            "frustrated": frustrated,
            "emotion": emotion_1,
            "color": color,
        },
    )


def export(request):
    document = Documents()
    dataset = document.export()
    response = HttpResponse(dataset.xls, content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="emotions.xls"'
    return response
