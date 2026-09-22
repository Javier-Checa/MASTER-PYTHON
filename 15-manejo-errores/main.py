"""
Capturar excepciones y manejar errores en código
susceptible a fallos/errores
"""
"""
try:
    
    nombre = input("¿Cuál es tu nombre?: ")

    if len(nombre) > 1:
        
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)

except:
    print("Ha ocurrido un error. Introduce un nombre, por favor.")
    
else:
    print("¡Genial! Todo ha funcionado correctamente.")
    
finally:
    print("¡¡¡Fin de la iteración!!!")
"""

# Manejo de múltiples excepciones

try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: " +str(numero**2))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código!!!")
#except ValueError:
    #print("Por favor, introduce un número correcto!!!")
except Exception as e:
    print(type(e))
    print("Lo siento, ha ocurrido un error: ", type(e).__name__)
