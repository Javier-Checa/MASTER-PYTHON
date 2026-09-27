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
);
""")


# Guardar cambios

conexion.commit()


# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
"""
cursor.execute("DELETE FROM productos")
conexion.commit()
"""

# Insertar muchos registros de golpe

productos = [
    ("Ordenador portátil", "Buen PC", 700),
    ("Teléfono Smartphone", "Gama media Motorola", 90),
    ("Smartwatch 3ª generación", "Con GPS y tensiómetro", 120),
    ("Robot de cocina", "Gama media Taurus", 240),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()


# Update (actualizar datos)

cursor.execute("UPDATE productos SET precio=550 WHERE precio=700")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 150;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Título:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")    
producto = cursor.fetchone()
print(producto)

# Cerrar conexión

conexion.close()

