"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único
nombre.
Para acceder a esos valores podemos usar un índice numérico, que empieza en 0.
"""

pelicula = "Batman"

# Definir lista

peliculas = ["Batman", "Spiderman", "El señor de los anillos", "Capitan America"]
cantantes = list(("David Bisbal", "Maluma", "Luis Fonsi", "Shakira"))
years = list(range(2020, 2050))
variada = ["David Bisbal", 34, True, "Maluma", 30]

"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# Indices
print(peliculas[0], peliculas[2]) # Acceder a un elemento de la lista
print(peliculas[-1]) # Acceder al último elemento de la lista
print(cantantes[1:3]) # Acceder a un rango de elementos de la lista
print(peliculas[0:]) # Acceder a un rango de elementos de la lista

peliculas[1] = "Gran Torino" # Modificar un elemento de la lista
print(peliculas)

# Añadir elementos a lista

cantantes.append("Adele") # Añadir un elemento al final de la lista
cantantes.append("Ed Sheeran") # Añadir un elemento al final de la lista
print(cantantes)


# Recorrer lista

print ("\n************* LISTADO PELÍCULAS ***************\n")
for pelicula in peliculas:
    print(pelicula)

print("\n")

