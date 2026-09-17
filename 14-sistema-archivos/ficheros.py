from io import open
import pathlib

# Abrir archivo

ruta = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_texto.txt"

archivo = open(ruta, "a+")


# Escribir dentro de un archivo
archivo.write("\n****** Zoy un tezto ezcrito por la Macu metido desde Python ******\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
contenido = archivo_lectura.read()

for elemento in contenido:
    print(elemento)

