from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)

def hola_mundo(request):
    return HttpResponse("""
        <h1>Hola mundo con Django!!</h1>
        <h3> Soy Javier Checa WEB</h3>
    """)