"""
# FOR

for variable in elemento_iterable (lista, rango, tupla, diccionario, conjunto, etc):
    BLOQUE DE INSTRUCCIONES

"""

"""
contador = 0
resultado = 0

for contador in range(0, 9):
    print("Voy por el "+ str(contador))
    resultado = resultado + contador

print(f"El resultado es: {resultado}")
"""


# Ejemplo tablas de multiplicar
print("\n############### EJEMPLO TABLAS DE MULTIPLICAR ###############\n")

numero_usuario = int(input("Introduce un número para mostrar su tabla de multiplicar: "))  

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n#### Tabla de multiplicar del {numero_usuario} ####")

for numero_tabla in range(1, 11):
    print(f"\n{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")    
else:
    print(f"\nTabla de multiplicar del número {numero_usuario} finalizada.\n")    
    print("\nGracias por usar el programa.\n")


