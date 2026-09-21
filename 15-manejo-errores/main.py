"""
Capturar excepciones y manejar errores en código
susceptible a fallos/errores
"""

try:
    
    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre) > 1:
        
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)

except:
    print("Ha ocurrido un error. Introduce un nombre, por favor.")
