import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='master_python',
    port=3306
)

print(database)


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        return self.nombre
    
    
    def identificar(self):
        return self.nombre
    
    