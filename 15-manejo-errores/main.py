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
"""
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
"""

# Excepciones personalizadas o lanzar excepciones.

try:
    nombre = input("Indroduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al Máster en Python, {nombre} !!!")
except ValueError:
    print("Introduce los datos como toca, cojones... que pareces tonto, joder!!!")
except Exception as e:
    print("Existe un error: ", e)

    