# Importar módulo sqlite que viene incorporado por defecto en Python

import sqlite3

# Conexión

conexion = sqlite3.connect('./19-bases-datos/pruebas.db')


# Crear cursor

cursor = conexion.cursor()


# Crear tabla

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo varchar(255),
    descripcion text,
    precio int(255)              
)
""")


# Guardar cambios

conexion.commit()


# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("Título:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")    
producto = cursor.fetchone()
print(producto)

# Cerrar conexión

conexion.close()

