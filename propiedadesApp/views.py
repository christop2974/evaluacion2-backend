import json
from pathlib import Path
from django.conf import settings
from django.shortcuts import render

def cargar_propiedades():
    ruta = Path(settings.BASE_DIR) / 'propiedadesApp' / 'data' / 'propiedades.json'
    with open(ruta, encoding='utf-8') as archivo:
        return json.load(archivo)

def inicio(request):
    propiedades = cargar_propiedades()
    destacadas = [p for p in propiedades if p.get('destacada')]
    if not destacadas:
        destacadas = propiedades[:3]
    return render(request, 'propiedadesApp/inicio.html', {'destacadas': destacadas[:3]})

def propiedades(request):
    lista = cargar_propiedades()
    tipo = request.GET.get('tipo', '').strip()
    comuna = request.GET.get('comuna', '').strip()
    if tipo:
        lista = [p for p in lista if p['tipo'].lower() == tipo.lower()]
    if comuna:
        lista = [p for p in lista if comuna.lower() in p['comuna'].lower()]
    tipos = sorted({p['tipo'] for p in cargar_propiedades()})
    comunas = sorted({p['comuna'] for p in cargar_propiedades()})
    return render(request, 'propiedadesApp/propiedades.html', {'propiedades': lista, 'tipos': tipos, 'comunas': comunas, 'tipo_actual': tipo, 'comuna_actual': comuna})
