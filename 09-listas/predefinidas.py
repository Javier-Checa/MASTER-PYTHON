cantantes = ["Shakira", "Maluma", "J Balvin", "Karol G", "Bad Bunny"]
numeros = [1, 2, 5, 8, 3, 4, 6, 7, 9, 10]

# Ordenar

print (numeros)
numeros.sort() # Ordenar de menor a mayor
print (numeros)

# Añadir elementos a lista
cantantes.append("Celine Dion") # Añadir un elemento al final de la lista
cantantes.insert(0, "Ricky Martin") # Añadir un elemento en una posición específica
#print(cantantes)

# Eliminar elementos de lista
cantantes.pop(1) # Eliminar un elemento en una posición específica
cantantes.remove("Bad Bunny") # Eliminar un elemento por su valor
# print(cantantes)

# Invertir orden de lista

numeros.reverse() # Invertir el orden de la lista
print(numeros)

# Buscar dentro de la lista
print(cantantes)
print("Maluma" in cantantes) # Buscar un elemento en la lista

# Contar elementos de una lista
print(len(cantantes)) # Contar el número de elementos en la lista

# Cuántas veces aparece un elemento en la lista
cantantes.append("Karol G")
print(cantantes.count("Karol G")) # Contar cuántas veces aparece un elemento en la lista

# Conseguir indice de un elemento en la lista
print(cantantes.index("J Balvin")) # Conseguir el índice de un elemento en la lista

# Unir listas
cantantes.extend(numeros) # Unir dos listas
print(cantantes)