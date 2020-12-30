from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('over-ons', views.over_ons, name='over-ons'),
]