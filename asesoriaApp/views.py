import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render

def asesoria(request):
    servicios = ['Compra de propiedades', 'Venta de propiedades', 'Orientación para arriendo']
    return render(request, 'asesoriaApp/asesoria.html', {'servicios': servicios})

def consejos(request):
    ruta = Path(settings.BASE_DIR) / 'asesoriaApp' / 'data' / 'consejos.json'
    with open(ruta, encoding='utf-8') as archivo:
        lista_consejos = json.load(archivo)
    return render(request, 'asesoriaApp/consejos.html', {'consejos': lista_consejos})
