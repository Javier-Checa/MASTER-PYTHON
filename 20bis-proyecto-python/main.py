"""
PROYECTO PYTHON Y MYSQL:
- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar notas, borrarlas.
  
"""

print("""
Acciones disponibles:
    - registro
    - login         
""")

accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    print("\nOk!! Vamos a registrarte en el sistema...")
    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")
    
    
    
elif accion == "login":
    print("Vale!! Identifícate en el sistema...")
    email = input("Introduce tu email: ")
    password = input("Introduce tu contraseña: ")
    
        