# Programación orientada a objetos (POO u OOP)

# Definir una clase (molde para crear más objetos de ese tipo)
# (Coche) con características similares

class Coche:

        # Atributos o propiedades (variables)
        # Carcacterísticas del coche
        color = "Rojo"
        marca = "Ferrari"
        modelo = "Aventador"
        velocidad = 300
        caballaje = 500
        plazas = 2

        # Métodos, que son acciones que hace el objeto (coche). Son las antiguas funciones.
        
        def setColor(self, color):
            self.color = color
            
        def getColor(self):
            return self.color
        
        def setModelo(self, modelo):
            self.modelo = modelo
            
        def getModelo(self):
            return self.modelo
        
        def acelerar(self):
            self.velocidad += 3 

        def frenar(self):
            self.velocidad -= 2

        def getVelocidad(self):
            return self.velocidad

# Fin definicion clase

# Crear objetos / Instanciar la clase


# Fin definicion clase

# Crear objetos / Instanciar la clase

coche = Coche()

print("\n--------- COCHE 1 ---------\n")

coche.setColor("Amarillo")
coche.setModelo("Testarossa")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()


print("Velocidad nueva: ", coche.getVelocidad())

print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

# Crear más objetos

coche2 = Coche()

print("\n---------- COCHE 2 ---------\n")

print(coche2.getColor())

print(coche2.marca, coche2.getModelo(), coche2.getColor())
