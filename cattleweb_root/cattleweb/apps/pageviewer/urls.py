from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('over-ons', views.over_ons, name='over-ons'),
    path('contact', views.contact, name='contact'),
    path('producten', views.producten, name='producten'),
    path('gallerij', views.gallerij, name='gallerij')
]