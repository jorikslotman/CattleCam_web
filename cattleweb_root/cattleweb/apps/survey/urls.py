from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('assess/<survey_id>', views.assess,name='assess'),
]