
def holaMundo(nombre):
    return f"Hola qué tal estás, {nombre}"


def calculadora(numero1, numero2, basicas = True):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma) + "\n"
        cadena += "Resta: " + str(resta) + "\n"

    else:
        cadena += "Multiplicación: " + str(multi) + "\n"
        cadena += "División: " + str(division) + "\n"

    return cadena


