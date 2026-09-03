"""
# BUCLE WHILE

Estructura de control que itera o repite la ejecución de una serie de instrucciones 
tantas veces como sea necesario, hasta que deje de cumplirse la condición.

while condición:
    BLOQUE DE INSTRUCCIONES 
    actualización de contador
    
"""

"""
contador = 1
while contador <= 100:
    print(f"Voy por el {contador}")
    contador += 1

print("\n ---------------------------------------- \n")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1
print(muestrame) 
"""


# Ejemplo

print("\n #### EJEMPLO #### \n")

numero_usuario = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1
print(f"\n#### Tabla de multiplicar del {numero_usuario} ####\n")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}\n")
    contador += 1   
else:
    print("\n Tabla de multiplicar finalizada \n")




