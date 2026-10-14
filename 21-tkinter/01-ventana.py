# Tkinter es un módulo de Python que se utiliza para crear interfaces gráficas de usuario (GUI). 
# A continuación, se muestra un ejemplo básico de cómo crear una ventana utilizando Tkinter:

from tkinter import *
import os.path


class Programa:
    def __init__(self):
        self.title = 'Master en Python con Tkinter para interfaz gráfica'
        self.icon = './imagenes/logotipo.ico'
        self.icon_alt = './21-tkinter/imagenes/logotipo.ico'
        self.size = '750x450'
        self.resizable = False  # Permitir o no cambiar el tamaño de la ventana
        
    def cargar(self):
        # Crear la ventana principal o raíz
        ventana = Tk()
        self.ventana = ventana  # Guardar la referencia de la ventana en el objeto

        # Título de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambiar el color de fondo de la ventana
        ventana.config(bg="lightyellow")

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)  # Ancho x Alto

        # Bloquear el cambio de tamaño del alto de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)
      
       
    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
        
        
    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre        
        self.ventana.mainloop()
        
        
# Instanciar mi programa
    
programa = Programa()
programa.cargar()

programa.addTexto("¡Hola, mundo!")
programa.addTexto("Yo soy")
programa.addTexto("un texto")
programa.addTexto("escrito para")
programa.addTexto("esta ventana")


programa.mostrar()

