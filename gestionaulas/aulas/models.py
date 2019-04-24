from django.db import models


class Aula(models.Model):
    capacidad = models.IntegerField()
    sector = models.CharField(max_length=250)
    nro_aula = models.IntegerField()



class Carrera(models.Model):
    nombre = models.CharField(max_length=250)


class Curso(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nivel = models.IntegerField()


class Materia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)


class Docente(models.Model):
    materia = models.ManyToManyField(Materia)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()


class Alumno(models.Model):
    carrera = models.ManyToManyField(Carrera)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()
    nro_registro = models.IntegerField()


class Disponibilidad(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()
