from django.http import HttpResponseRedirect
from django.shortcuts import render
from hosting.models import Photo
from hosting.helpers import get_statistics_from_image


def index(request):
    return render(request, 'index.jinja2')


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.jinja2', {'photos': photos})


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


def photo(request, id):
    image = Photo.objects.get(id=id)
    statistics = image.statistic.split(',')
    if request.method == "POST":
        image.image.delete(True)
        image.delete()
    try:
        return render(request, 'photo.jinja2', {'image': image, 'statistics': statistics})
    except ValueError:
        return HttpResponseRedirect('/hosting/gallery/')
