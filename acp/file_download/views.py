from django.shortcuts import render

def download(request):

    return render(request, 'file_download/download.html', { 'title': 'Download File'})
