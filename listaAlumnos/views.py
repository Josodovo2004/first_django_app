from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno, Curso, AlumnoCurso

# Create your views here.

def index(request):
    return render(request, 'listaAlumnos/index.html')

def lAlumnos(request):
    alumnos = Alumno.objects.all()

    output = ",".join([a.nombreAlumno for a in alumnos])

    return render(request, 'listaAlumnos/lAlumnos.html', output)

def lCursos(request):
    pass

def AlumnosPorCurso(request):
    pass