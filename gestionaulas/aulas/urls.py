from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('horarios', views.horarios, name='horarios')
]
