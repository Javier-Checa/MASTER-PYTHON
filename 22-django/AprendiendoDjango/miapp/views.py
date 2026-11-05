from django.shortcuts import render, HttpResponse

# Crea tu vista aquí.
# MVC = Modelo Vista Controlador -> Acciones (métodos)
# MVT = Modelo Template Vista -> Acciones (métodos)

def holaMundo(request):
    return HttpResponse("¡Hola, Mundo, con Django!")
