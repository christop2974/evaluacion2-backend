from django.urls import include, path
urlpatterns = [
    path('', include('propiedadesApp.urls')),
    path('asesoria/', include('asesoriaApp.urls')),
]
