from django.http import HttpResponse
import random
from django.shortcuts import render
from django.template import Context, Template


def inicio(request):
    return render(request, "indice/index.html", {})

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>                       
                        ''')
    
def numero_random(request):
    numero = random.randrange(15,1000000)
    texto = f'<h1>Aluquita {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero random {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    # plantilla = open(r"C:\Users\USUARIO\Desktop\Proyecto Gabriel\indice\plantilla\mi_plantilla.html")
    
    # template = Template(plantilla.read())
    
    nombre = ''
    apellido = 'Graterol'
    lista = ["Aluquita", "Melanie y mi amor Ariani"]
    
    diccionario_de_datos = {
    'nombre': nombre,
    'apellido': apellido,
    'nombre_largo': len(nombre),
    'lista': lista
    }   

    
    
    # context = Context(diccionario_de_datos)
    
    # plantilla_preparada = template.render(context)
    
    # return HttpResponse(plantilla_preparada)

    return render(request,"indice/mi_plantilla.html",diccionario_de_datos)