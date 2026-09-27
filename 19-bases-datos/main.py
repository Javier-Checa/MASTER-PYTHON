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

cursor = database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
