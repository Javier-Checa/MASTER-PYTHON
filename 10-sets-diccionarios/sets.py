"""
SET es un tipo de dato, para tener una colección de valores,
pero no tiene ni índice ni orden, y no permite elementos duplicados.
"""

personas = {"Juan", "Pedro", "Maria", "Ana", "Juan"} # No permite elementos duplicados
personas.add("Luis") # Añadir un elemento al set
personas.remove("Ana") # Eliminar un elemento del set
print(type(personas)) # <class 'set'>
print(personas)
