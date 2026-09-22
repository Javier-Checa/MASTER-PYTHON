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
        
        def acelerar(self):
            self.velocidad += 3 

        def frenar(self):
            self.velocidad -= 2

        def getVelocidad(self):
            return self.velocidad

# Fin definicion clase

# Crear objetos / Instanciar la clase

coche = Coche()

print(coche.marca, coche.modelo, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()


print("Velocidad nueva: ", coche.velocidad)