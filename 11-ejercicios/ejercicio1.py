"""
Ejercicio 1: Crear un programa que tenga una lista de 8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla en pantalla.
- Hacer una función que recorra listas de números y devuelva un strig.
- Ordenarla y mostrarla.
- Mostrar su longitud.
- Buscar algún elemento (que el usuario pida por teclado).
"""

# Crear la lista

numeros = [ 13, 64, 52, 73, 21,7, 91, 63]

# Crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += "Elemento " + str(elemento)
        resultado += "\n"
    
    return resultado
        

# Recorrer y mostrar

print ("######### Recorrer y mostrar #########")

"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))
print(mostrarLista(["Juan", "Pepe", "Manuel"]))