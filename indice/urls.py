from django.urls import path

from .views import inicio, mi_plantilla, numero_del_usuario, otra_vista, numero_random

urlpatterns = [ 
               
    path('', inicio, name="inicio"),
    path('otra_vista', otra_vista, name="otra_vista"),
    path('numero-random/', numero_random, name="numero_random"),
    path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plan/', mi_plantilla, name="mi_plantilla"),  
]
