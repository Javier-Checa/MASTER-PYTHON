"""
Una variable es un contenedor de información
que dentro guardará un dato; se pueden crear 
muchas varialbes y que cada una tenga un dato distinto.
"""

texto = "Máster en Python"
texto2 = "con Víctor Robles"
numero = 53
decimal = 3.1416


print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------")

numero = 38
decimal = 2.2345


print(numero)
print(decimal)


print("-------------------------------")

# Concatenación de variables
nombre = "Javier" 
apellidos = "Checa Martínez"
web = "www.javiercheca.es"

# print(nombre +" " + apellidos+" - " + web)

# print(f"{nombre} {apellidos} - {web}") # f-string

print("Hola, me llamo {} {} y mi web es: {}".format(nombre, apellidos, web)) # format

print(nombre, apellidos, web) # print con varias variables



