"""
Ejercicio 5. Hacer un programa que muestre todos los números que hay 
entre dos números que quiera el usuario.
"""

numero1 = int(input("\nIntroduce el primer número: "))
numero2 = int(input("\nIntroduce el segundo número: "))
print ("\n")

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        
        print(contador)
else:
    print("\nEl primer número debe ser menor que el segundo\n")