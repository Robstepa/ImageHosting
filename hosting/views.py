from django.shortcuts import render
from ImageHosting import settings
from hosting.models import Photo
from hosting.helpers import get_filename_from_path, get_statistics_from_image


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
    VALID_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]
    info = ''
    if request.method == 'POST':
        file = request.FILES['photo']
        if file.name.split('.')[-1] in VALID_IMAGE_EXTENSIONS:
            Photo(statistic=get_statistics_from_image(file)).image.save('img.jpg', file, True)
            info = 'Done'
        else:
            info = "Upload an image, please"
    return render(request, 'upload.jinja2', {'info': info})
