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


# Lista con diccionarios

contactos = [
    {
        "nombre": "Ana",
        "email": "ana.garcia@example.com"
    },
    {
        "nombre": "Luis",
        "email": "luis.lopez@example.com"
    },
    {
        "nombre": "Maria",
        "email": "maria.rodriguez@example.com"
    }
]

contactos[0]["nombre"] = "Anita" # Modificar el valor de una clave
print(contactos[0]["nombre"]) # Anita
print(contactos[1]["email"]) # luis.lopez@example.com
print(contactos[2]["nombre"]) # Maria  

print("\nListado de contactos: ")
print("--------------------------------------------------")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}, Email: {contacto['email']}")
    print("--------------------------------------------------")
