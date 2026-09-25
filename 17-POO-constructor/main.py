from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 220, 4)
carro1 = Coche("Rojo", "Citroën", "XSara", 160, 230, 5)
carro2 = Coche("Gris oscuro", "Seat", "Leon", 180, 240, 5)
carro3 = Coche("Azul metalizado", "Volkswagen", "Polo", 200, 250, 5)




print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())


# Detectar tipado

# carro3 = "Es string aleatorio"
if type(carro3) == Coche:
    print("\n¡¡¡Es un objeto correcto!!!    :-)\n")
else:
    print("\nNo es un objeto :-( \n")
    
    
# Visibilidad

print(carro.soy_publico)
# print(carro.__soy_privado)
print(carro.getPrivado())    






