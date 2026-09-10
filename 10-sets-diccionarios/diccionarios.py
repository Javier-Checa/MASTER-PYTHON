"""
DICCIONARIO:
Es una colección de datos que almacena pares de clave y valor.
Es parecido a un array asociativo o un objeto json en otros lenguajes de programación.
Los diccionarios son mutables, lo que significa que se pueden cambiar después de su creación
"""


persona = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "email": "juan.perez@example.com"
}

print(type(persona)) # <class 'dict'>
print(persona["nombre"])
print(persona["edad"])
print(persona.get("email")) # Obtener el valor de una clave


