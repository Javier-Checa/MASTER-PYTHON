from io import open
import pathlib
import shutil

# Abrir archivo

ruta = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_texto.txt"

archivo = open(ruta, "a+")


# Escribir dentro de un archivo
archivo.write("****** Zoy un tezto ezcrito por la Macu metido desde Python ******\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)
    # print("- "+frase.capitalize())
    
# Copiar archivos

"""
ruta_original = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_copiado.txt"
ruta_alternativa = str("./07-ejercicios/fichero-copiado77.txt") 

shutil.copyfile(ruta_original, ruta_nueva)    
"""

# Mover y renombrar archivos
"""
ruta_original = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""


# Eliminar archivos
"""
import os
ruta_nueva = str(pathlib.Path().absolute()) + "./14-sistema-archivos/fichero_copiado_NUEVO.txt"

os.remove(ruta_nueva)
"""

# Comprobar si un archivo existe

import os.path

# print(os.path.abspath("./"))
ruta_comprobar = os.path.abspath("./") + "./14-sistema-archivos/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")