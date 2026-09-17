"""
Módulos: son funcionalidades ya hechas para reutilizar. También se suelen llamar librerías.
En Python hay muchos módulos, que los puedes consultar aquí:

https://docs.python.org/3/library/

Podemos conseguir módulos que ya vienen en el lenguaje,
módulos en internet, y también podemos crear nuestros modulos.
"""

# Importar modulo propio

# import mimodulo
# from mimodulo import holaMundo

from mimodulo import *

print(holaMundo("Javier Checa Page"))
print(calculadora(3, 5, True))

#print(mimodulo.calculadora(3, 5, True))

# Módulo de fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha y hora en formato personalizado es: ", fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

# Módulo matemáticas

import math

print("Raíz cuadrada de 2: ", math.sqrt(2))

print("Número pi: ", math.pi)

print("Número e o número de Napier: ", float(math.e))

print("Número redondeado al alza:", math.ceil(3.141592653589793))

print("Número redondeado a la baja:", math.floor(3.141592653589793))


# Módulo ramdom

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))