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

print("\n######### Recorrer y mostrar #########")

"""
for numero in numeros:
    print(numero)
"""

print(mostrarLista(numeros))
print(mostrarLista(["Juan", "Pepe", "Manuel"]))

# Ordenar y mostrar
print("######### Ordenar y mostrar #########")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar longitud
print("######### Mostrar longitud #########")
print("\n",len(numeros),"\n")

# Búsqueda en la lista
print("######### Búsqueda en la lista #########")

busqueda = int(input("Introduce el número: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"####### Buscar en la lista el número {busqueda} #########")

search = numeros.index(busqueda)
print(f"El número buscado existe en la lista, es el índice: {search}")