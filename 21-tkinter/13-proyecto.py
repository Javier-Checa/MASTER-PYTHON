"""
Crear un progrma que tenga:
- (hecho) - Ventana
- (hecho) - Tamaño fijo de la ventana
- (hecho) - No redimensionable
- (hecho) - Un menú
- (hecho) - Opción de salir 
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente sin usar una base de datos
- Mostrar los datos listados en la pantalla principal o home (landing)

"""
from tkinter import *


# Definir ventana
ventana = Tk()
ventana.geometry("800x500")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

# Pantallas
def home():
    home_label = Label(ventana, text= "Inicio")
    home_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
    
    
    return True

def add():
    return True

def info():
    return True


# Cargar pantalla inicio
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio")
menu_superior.add_command(label="Añadir")
menu_superior.add_command(label="Información")
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)


# Cargar ventana
ventana.mainloop()
