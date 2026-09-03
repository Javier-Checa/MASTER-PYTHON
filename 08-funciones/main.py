"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo un nombre
concreto que pueden reutilizarse invocando a la función tantas veces
como sea necesario.

def nombreDeMiFunción(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)
"""
# Ejemplo 1




# Definir función

def muestraNombre():
    print("Javier")
    print("Jaime")
    print("Francisco")
    print("Rubén")
    print("Pablo")
    print("Pedro")
    print("Rafael")
    print("\n")

# Invocar función

muestraNombre()
muestraNombre()
muestraNombre()

"""
# Ejemplo 2

print("######## EJEMPLO 2 ########\n")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}\n")
    if edad >= 18:
        print("Eres mayor de edad\n")
    else: 
        print("Eres menor de edad\n")
           
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print("\n")
mostrarTuNombre(nombre, edad)

"""

# Ejemplo 3

print("######## EJEMPLO 3 ########\n")

def tabla(numero):
    print(f"Tabla de multiplicar del número {numero}\n")
    
       
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")

tabla(15)
tabla(17)
tabla(19)
tabla(21)

print("\n")


print("######## EJEMPLO 3.1 ########\n")
for numero_tabla in range(1, 11):
    tabla(numero_tabla)


# Ejemplo 4: Función con parámetros opcionales

print("######## EJEMPLO 4 ########\n")

# Parámetros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO\n")
    print(f"Nombre: {nombre}\n")
    
    if dni != None:
        print(f"DNI: {dni}\n")
            
getEmpleado("Javier")
getEmpleado("María", "87654321B")



# Ejemplo 5: Función con retorno de valores
def suma(numero1, numero2):
    return numero1 + numero2

resultado = suma(5, 3)
print(f"El resultado de la suma es: {resultado}")
