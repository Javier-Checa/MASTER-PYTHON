"""
Escribir un programa que muestre por pantalla los cuadrados (un número multiplicado por si mismo)
de los primeros 60 números naturales. Resolverlo con el bucle while y con el for.
"""

#   WHILE
"""
contador = 0
while contador <= 60:
    cuadrado = contador**2
    print(f"El cuadrado de {contador} es ---->>> {cuadrado}")
    contador += 1
"""

#   FOR
for numero in range(61):
    cuadrado = numero**2
    print(f"El cuadrado de {numero} es ---->>> {cuadrado}")