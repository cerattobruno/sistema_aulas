from django.shortcuts import render


from .models import Aula

def horarios(request):
   #data = {"aula":{"17":"Matematica", "17_40":"Matematica", "18_20":"Programacion"}}
   h17 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h17_40 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h18_20 = ["Mat 2", "Mat 2", "Prog 2", "Leng 2", "Sociales 2", "Ingles 2"]
   h19 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h19_40 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h20_20 = ["Mat 2", "Mat 2", "Prog 2", "Leng 2", "Sociales 2", "Ingles 2"]
   h21 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h21_40 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   h22_20 = ["Mat 2", "Mat 2", "Prog 2", "Leng 2", "Sociales 2", "Ingles 2"]
   h23 = ["Mat", "Mat", "Prog", "Leng", "Sociales", "Ingles"]
   horarios = {"17:00":h17, "17:40":h17_40, "18:20":h18_20, "19:00":h19, "19:40":h19_40, "20:20":h20_20,
               "21:00":h21, "21:40":h21_40, "22:20":h22_20, "23:00":h23}
   return render(request, "cuadro.html", {"aulas":Aula.objects.all(), "horarios":horarios})
