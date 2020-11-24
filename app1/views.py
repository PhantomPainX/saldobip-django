from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def inicio(request):

   return render(request, "index.html")

def resultado(request):

   idbip = request.GET['tid']

   if len(idbip) <= 3 :
      return render(request, "error_null_field.html")
   else:
      try:

         apilink="http://bip-servicio.herokuapp.com/api/v1/solicitudes.json?bip=%d" % int(request.GET['tid'])
         response = requests.get(apilink)
         contenido = json.loads(response.text)
         print(contenido)

         try:
            if contenido['fechaVencimiento']:
               return render(request, "vencido.html", contenido)
         except:
            return render(request, "resultado.html", contenido)

      except:
         return render(request, "error_string_id.html")
