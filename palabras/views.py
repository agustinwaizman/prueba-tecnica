from datetime import datetime
from turtle import update
from django.shortcuts import render, redirect
from .models import Palabra
"""
la funcion index recibe una solicitud http y renderiza el template index.html teniendo todos los elementos como contexto
mediante 'palabras = Palabra.objects.all()' obtenemos mediante un Queryset todos los objetos Palabra almacenados en la base de datos.

Mediante la funcion register realizamos lo siguiente:
* Comparar si la palabra es un palindromo removiendo los espacios en caso de que sea una frase
* Verificar si esa palabra o frase ya esta almacenada en nuestra base de datos.
* En caso de que este almacenada actualizara su ultimo ingreso
* En caso de que no lo esté creara este objeto
"""
def verificarPalindromo(text:str):
    text = text.replace(' ','')
    text = text.lower()
    if text == text[:: -1]:
        return True
    else:
        return False

def index(request):
    palabras = Palabra.objects.all() # obtenemos mediante un Queryset todos los objetos Palabra almacenados en la base de datos.
    return render(request, 'index.html', { 'palabras':palabras }) # Renderizamos el template index.html pasandole como contexto todos los elementos obtenidos mediante el Queryset anterior

def register(request):
    entrada = request.POST['txtWord'] # Obtenemos la solicitud post enviada mediante nuestro formulario.
    pal = str(entrada) # Convertimos la solicitud en un texto apto para poder utilizarlo y comparar si ya esta registrado en nuestra base de datos

    esPalindromo = verificarPalindromo(pal)

    existe = Palabra.objects.filter(contenido=str(entrada)).exists() # Filtramos los Queryset almacenados en nuestra DB por el valor contenido para verificar si esta registrado en nuestra DB. El metodo .exist() nos devolvera True si se encuentra almacenado en nuestro Queryset, y retornara False en caso de que no lo esté.
    if existe: 
        Palabra.objects.update(update=datetime.now()) # Si ya esta almacenado en nuestra base de datos solamente actualizaremos la ultima vez que fue ingresado
    else:
        palabras = Palabra.objects.create(contenido=entrada, esPalindromo=esPalindromo) # Si no esta registrada previamente añadiremos la palabra a nuestra base de datos
    return redirect('palabras:index') # Redirigimos a nuestra vista principal.