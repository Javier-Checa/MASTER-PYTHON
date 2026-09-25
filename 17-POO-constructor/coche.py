class Coche:

        # Atributos o propiedades (variables)
        # Carcacterísticas del coche
        color = "Rojo"
        marca = "Ferrari"
        modelo = "Aventador"
        velocidad = 300
        caballaje = 500
        plazas = 2
        
        soy_publico = "Hola, soy un atributo público."
        __soy_privado = "Hola, soy un atributo privado."
        
        """
        Definición del constructor: método especial dentro de una clasees un método especial 
        de una clase que se ejecuta automáticamente cuando se crea (instancia) 
        un nuevo objeto de esa misma clase.
        Su función principal es inicializar el objeto, es decir, asignarle un estado inicial válido
        estableciendo los primeros valores de sus atributos antes de que 
        el programa empiece a utilizarlo.
        """
        
        def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
            self.color = color
            self.marca = marca
            self.modelo = modelo
            self.velocidad = velocidad
            self.caballaje = caballaje
            self.plazas = plazas

        # Métodos, que son acciones que hace el objeto (coche). Son las antiguas funciones.
        
        def getPrivado(self):
            return self.__soy_privado
              
        
        def setColor(self, color):
            self.color = color
            
        def getColor(self):
            return self.color
        
        def setModelo(self, modelo):
            self.modelo = modelo
            
        def getModelo(self):
            return self.modelo
        
        def setMarca(self, marca):
            self.marca = marca
            
        def getMarca(self):
            return self.marca
                
        def acelerar(self):
            self.velocidad += 3 

        def frenar(self):
            self.velocidad -= 2

        def getVelocidad(self):
            return self.velocidad

        def getInfo(self):
            
            info = "---- Información del coche ----"
            info += "\n Color: " + self.getColor()
            info += "\n Marca: " + self.getMarca()
            info += "\n Modelo: " + self.getModelo()
            info += "\n Velocidad: " + str(self.getVelocidad())
            
            return info
            
            
# Fin definición de clase            