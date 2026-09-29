import mysql.connector

# Conexión a base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

# ¿Ha sido la conexión correcta?
# print(database)

# CURSOR

cursor = database.cursor()

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# Crear tablas

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modero varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)                              
""")


cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 21500)")
database.commit()