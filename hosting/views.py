from django.http import HttpResponseRedirect
from django.shortcuts import render
from hosting.models import Photo
from hosting.helpers import get_statistics_from_image, is_valid_type


def index(request):
    return render(request, 'index.jinja2')


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.jinja2', {'photos': photos})


def upload(request):
    info = 'Please, browse first'
    if request.method == 'POST':
        file = request.FILES['photo']
        if is_valid_type(file):
            image_info = get_statistics_from_image(file)
            if isinstance(image_info, str):
                info = image_info
            else:
                Photo(statistic=image_info).image.save('img.jpg', file, True)
                info = 'Done, now you can select another image'
        else:
            info = "Upload an image type of: JPG, PNG, JPEG"
    return render(request, 'upload.jinja2', {'info': info})


def photo(request, image_id):
    image = Photo.objects.get(id=image_id)
    statistics = image.statistic.split(',')
    return render(request, 'photo.jinja2', {'image': image, 'statistics': statistics})


def delete(request, image_id):
    image = Photo.objects.get(id=image_id)
    image.image.delete(True)
    image.delete()
    return HttpResponseRedirect('/hosting/gallery/')
