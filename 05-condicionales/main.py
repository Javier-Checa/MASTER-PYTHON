"""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Ejecutar otro grupo de instrucciones

if condicion:
    instrucciones
else
    otras instrucciones

# Operadores de comparación
== igual
!= diferente
<  menor que
> mayor que
<= menor o igual que
>= mayor o igual que


# Operadores lógicos
and Y
or  O
not NO
!   negación

"""

"""
# Ejemplo 1
print("############### EJEMPLO 1 ###############")

# COLOR = "verde"
color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
    print("¡¡¡Enhorabuena!!!")
    print("Has adivinado mi color favorito.")
else:
    print("¡Ohhh, lo siento! No has adivinado mi color favorito. ¡Era el color rojo!")

"""

"""
# Ejemplo 2
print("############### EJEMPLO 2 ###############")

year = int(input("¿En qué año estamos? "))

if year >= 2026:
    print("Estamos en el año 2026 o en un año posterior.")      
else:
    print("Estamos en un año anterior al 2026.")    

"""

"""
# Ejemplo 3     
print("############### EJEMPLO 3 ###############")

nombre = "Javier Checa"
ciudad = "Madrid"
continente = "Europa"
edad = 53
mayoria_edad = 18   

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad.")

    if continente != "Europa":
        print(f"{nombre} NO es europeo.")
    else:
        print(f"{nombre} es europeo y vive en {ciudad}.")  

else:
    print(f"{nombre} NO es mayor de edad.")

"""

"""
    
# Ejemplo 4     
print("############### EJEMPLO 4 ###############")

dia = int(input("Introduce el número del día de la semana (1-7): "))

if dia == 1:
    print("Es lunes.")  
else:
    if dia == 2:
        print("Es martes.")
    else:
        if dia == 3:
            print("Es miércoles.")
        else:
            if dia == 4:
                print("Es jueves.")
            else:
                if dia == 5:
                    print("Es viernes.")
                else:
                    if dia == 6:
                        print("Es sábado.")
                    else:
                        if dia == 7:
                            print("Es domingo.")
                        else:
                            print("El día introducido no es válido.")
"""

"""
if dia == 1:
    print("Es lunes.")
elif dia == 2:
    print("Es martes.")     
elif dia == 3:
    print("Es miércoles.")  
elif dia == 4:
    print("Es jueves.")
elif dia == 5:
    print("Es viernes.")
elif dia == 6:
    print("Es sábado.")
elif dia == 7:
    print("Es domingo.")
elif dia < 1 or dia > 7:
    print("El día introducido no es válido.")

"""

"""
# jemplo 5     
print("############### EJEMPLO 5 ###############")

edad_minima = 18
edad_maxima = 65    
edad_oficial = int(input("Introduce tu edad: "))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Estás en edad de trabajar.")
else:
    print("No estás en edad de trabajar.")

"""

"""
# jemplo 6     
print("############### EJEMPLO 6 ###############")

pais = input("Introduce el nombre del país: ")

if pais == "México" or pais == "España" or pais == "Colombia" or pais == "Venezuela" or pais == "Perú" or pais == "Argentina" or pais == "Chile" or pais == "Ecuador" or pais == "Guatemala" or pais == "Cuba":
    print(f"{pais} es un país de habla hispana.")   
else:
    print(f"{pais} no es un país de habla hispana.")

"""

"""
# Ejemplo 7     
print("############### EJEMPLO 7 ###############")

pais = input("Introduce el nombre del país: ")

if not (pais == "México" or pais == "España" or pais == "Colombia" or pais == "Venezuela" or pais == "Perú" or pais == "Argentina" or pais == "Chile" or pais == "Ecuador" or pais == "Guatemala" or pais == "Cuba"):
    print(f"{pais} NO es un país de habla hispana.")   
else:
    print(f"{pais} SÍ es un país de habla hispana.")

"""

# Ejemplo 8     
print("############### EJEMPLO 8 ###############")

pais = input("Introduce el nombre del país: ")

if pais != "México" and pais != "España" and pais != "Colombia" and pais != "Venezuela" and pais != "Perú" and pais != "Argentina" and pais != "Chile" and pais != "Ecuador" and pais != "Guatemala" and pais != "Cuba":
    print(f"{pais} NO es un país de habla hispana.")   
else:
    print(f"{pais} SÍ es un país de habla hispana.")
