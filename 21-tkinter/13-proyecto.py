"""
Crear un progrma que tenga:
- Ventana
- Tamaño fijo de la ventana
- No redimensionable
- Un menú
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente sin usar una base de datos
- Mostrar los datos listados en la pantalla principal o home (landing)
- Opción de salir 
"""
from tkinter import *

ventana = Tk()
ventana.geometry("900x500")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

ventana.mainloop()
