from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.jinja2')


def gallery(request):
    gallery = [1, 2, 3]
    return render(request, 'gallery.jinja2', {'gallery': gallery})


def upload(request):
    return render(request, 'upload.jinja2')
