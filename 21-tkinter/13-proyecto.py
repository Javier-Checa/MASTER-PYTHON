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
    add_label = Label(ventana, text= "Añadir producto")
    add_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    
    return True

def info():
    info_label = Label(ventana, text= "Información del producto")
    info_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    return True


# Cargar pantalla inicio
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menú
ventana.config(menu=menu_superior)


# Cargar ventana
ventana.mainloop()
