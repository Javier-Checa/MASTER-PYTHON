"""
Ejercicio 8. ¿Cuánto es el x por cieto de un número? Calculadora de porcentajes.
"""

numero = int(input("Introduce el número: "))

porcentaje = int(input(f"¿Qué porcentaje quieres sacar de {numero}? "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje} % de {numero} es: {operacion}")


