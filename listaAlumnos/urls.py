from django.urls import path

from . import views

app_name = "listaAlumnos"

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.lAlumnos, name= "lAlumnos")]