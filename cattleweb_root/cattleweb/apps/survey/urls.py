from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('assess/<survey_id>', views.assess, name='assess'),
    path('assess/<survey_id>', views.assess, name='process'),
    path('thanks', views.thanks, name='thanks'),
]