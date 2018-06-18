from django.urls import path

from hosting import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/photo/<int:image_id>', views.photo, name='photo'),
    path('gallery/delete/<int:image_id>', views.delete, name='delete')
]
