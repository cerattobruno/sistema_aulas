from django.contrib import admin

from .models import Carrera, Aula, Curso, Docente, Materia, Disponibilidad



admin.site.register(Carrera)
admin.site.register(Aula)
admin.site.register(Curso)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Disponibilidad)
