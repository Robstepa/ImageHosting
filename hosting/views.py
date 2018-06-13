from django.shortcuts import render

from ImageHosting import settings
from hosting.models import Photo
from hosting.helpers import get_filename_from_path

# Create your views here.


def index(request):
    return render(request, 'index.jinja2')


def gallery(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        name = get_filename_from_path(request.POST.get("photo"))
        image = Photo.objects.get(image=name)
        image.image.delete(True)
        image.delete()
    return render(request, 'gallery.jinja2', {'photos': photos, 'media_url': settings.MEDIA_URL})


def upload(request):
    info = ''
    if request.method == 'POST':
        Photo().image.save('img.jpg', request.FILES['photo'], True)
        info = 'Done'
    return render(request, 'upload.jinja2', {'info': info})
