from django.urls import path
from . import views

urlpatterns = [
    path('', views.horarios, name='horarios')
]
