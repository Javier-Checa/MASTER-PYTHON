from django.shortcuts import render, HttpResponse

# Crea tu vista aquí.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)

def hola_mundo(request):
    return HttpResponse("""
        <h1>¡Hola, Mundo, con Django!</h1>
        <p>Este es mi primer proyecto con Django</p>""")
