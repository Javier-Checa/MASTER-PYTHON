import os, shutil

# Crear carpeta
"""
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe este directorio")
"""

# Eliminar una carpeta
# os.rmdir("./mi_carpeta")


# Copiar carpetas
"""
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

print("\n*** CONTENIDO DE MI CARPETA ***\n")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)
print("\n")


