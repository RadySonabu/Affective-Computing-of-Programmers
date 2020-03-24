from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, "dashboard/home.html", {"title": "Upload Success"})

def about(request):

    return render(request, "dashboard/about.html", {"title": "About"})