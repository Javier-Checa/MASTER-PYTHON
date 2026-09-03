"""
Ejercicio 4. Pedir dos números al usuario y hacer todas las operaciones básicas
de una calculadora (suma, resta, multiplicación, división y potenciación)
y mostrarlos por pantalla
"""
\
print ("\n ### Introduzca los números enteros que se van a operar ### ")
numero1 = int(input("\nIntroduzca el primer número: "))
numero2 = int(input("\nIntroduzca el segundo número: "))

print(f"\nSuma: {numero1 + numero2}")
print(f"\nResta: {numero1 - numero2}")
print(f"\nMultiplicación: {numero1 * numero2}")

if numero2 != 0:
    print(f"\nDivisión: {numero1 / numero2}")
else:
    print("\nDivisión: ¡¡¡No se puede dividir entre cero!!!")

print(f"\nPotenciación: {numero1 ** numero2}\n")