from django.urls import path

from hosting import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery')
]
