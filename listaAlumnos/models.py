from django.db import models

# Create your models here.


class Alumno(models.Model):
    nombreAlumno = models.CharField(max_length = 50)
    apellidoAlumno = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.nombreAlumno + ' ' + self.apellidoAlumno)


class Curso(models.Model):
    nombreCurso = models.CharField(max_length = 25)

    def __str__(self):
        return self.nombreCurso
    

class AlumnoCurso(models.Model):
    idAlumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    idCurso = models.ForeignKey(Curso, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.idAlumno.nombreAlumno} esta en {self.idCurso.nombreCurso}"