from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Curso, Alumno

# Create your views here.

class IndexView(generic.ListView):
    template_name = "registroCursos/index.html"
    context_object_name = "cursos_set"

    def get_queryset(self) -> QuerySet[Any]:
        return Curso.objects.all()
    
class AlumnosCurso(generic.ListView):
    template_name = "registroCursos/AlumnosCurso.html"
    context_object_name = "alumnoCurso_set"

    def get_queryset(self) -> QuerySet[Any]:
        curso_id = self.kwargs['pk']
        return  Alumno.objects.filter(curso_id = curso_id)
    