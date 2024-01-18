from django.urls import path
from . import  views

app_name = "registroCursos"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.AlumnosCurso.as_view(), name='AlumnosCurso'),

]