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

"""
cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)
"""    


#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 21500)")
coches = [
    ('Seat', 'Ibiza', 19000),
    ('Renault', 'Megane', 19500),
    ('Volkswagen', 'Polo', 23000),
    ('Skoda', 'Fabia', 22500),
]

# cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio <= 20000 AND marca = 'Renault'")

result = cursor.fetchall()

print("---- TODOS MIS COCHES ----")
for coche in result:
    print(coche[0], coche[1], coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print (coche)