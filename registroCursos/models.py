from django.db import models

# Create your models here.


class Curso(models.Model):

    nombreCurso = models.CharField(max_length = 50)

    def __str__(self):
        return self.nombreCurso
    
class Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    nombreAlumno = models.CharField(max_length = 50) 
    apelidoAlumno = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.nombreAlumno + " " + self.apelidoAlumno)