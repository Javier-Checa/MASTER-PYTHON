"""
Ejercicio 3: Hacer un programa que compruebe si una variable está vacia y si
está vacia, rellenarla con texto en minúscula y mostrarlo
en mayúsculas.
"""

texto = " "

if len(texto.strip()) <= 0:

    texto = "hola zoy un tezto de la macu y eztoy en minuhculaz, ozú"
    print(texto.upper())

else:
    print(f"La variable tiene contenido {texto}")