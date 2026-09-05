nombre = "Javier Checa"

#Funciones generales
print(nombre)
print(type(nombre))  # Tipo de dato
print(len(nombre))  # Longitud de la cadena
print(nombre.upper())  # Convertir a mayúsculas
print(nombre.lower())  # Convertir a minúsculas

# Detectar el tipado
comprobar = isinstance(nombre, str)  # Comprobar si es una cadena

if comprobar:
    print("La variable es una cadena de texto")
else:
    print("La variable no es una cadena de texto")

if not isinstance(nombre, float):
    print("La variable no es un número con decimales")
else:
    print("La variable es un número con decimales")


# Limpiar espacios
frase = "   mi contenido tiene muchos espacios al principio y al final   "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2026
print(year)
# del year  # Eliminar variable   
# print(year)  # Esto dará error porque la variable ya no existe

# Comprobar variable vacía
texto = " ffaasstt "
if len(texto.strip()) == 0:
    print("La variable está vacía")
else:
    print("La variable tiene contenido,", len(texto.strip()), "caracteres")

# Encontrar caracteres
frase = "Carpe diem, aprovecha el día"
print(frase.find("die"))  # Devuelve la posición de la palabra

nueva_frase = frase.replace("Carpe diem", "Campa y ríe")  # Reemplaza palabras
print(nueva_frase)
