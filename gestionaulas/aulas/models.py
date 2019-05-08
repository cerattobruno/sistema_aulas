from django.db import models


class Aula(models.Model):
    capacidad = models.IntegerField()
    sector = models.CharField(max_length=250)
    nro_aula = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.sector, self.nro_aula)



class Carrera(models.Model):
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nivel = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.nivel, self.carrera)


class Materia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Docente(models.Model):
    materia = models.ManyToManyField(Materia)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    dni = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Disponibilidad(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fin = models.TimeField()

    def __str__(self):
        return "{} - {} - {} - {}".format(self.aula, self.materia, self.horario_inicio, self.horario_fin)


