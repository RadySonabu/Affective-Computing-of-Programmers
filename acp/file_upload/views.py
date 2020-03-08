from django.shortcuts import render, redirect
from .forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'file_upload/upload.html', {
        'form': form, 'title':'Upload File',
    })
