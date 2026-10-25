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
# Mostrar pantalla    
    
    home_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)
    
    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()    
    
    return True

def add():
    add_label.config(
        fg= "white",
        bg= "green",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)
    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()  
    
    return True

def info():
    info_label.config(
        fg= "white",
        bg= "blue",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    data_label.grid(row=1, column=0)
    
    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    
    return True

# Definir campos de pantalla (INCIO)
home_label = Label(ventana, text= "Inicio")

# Definir campos de pantalla (ADD)
add_label = Label(ventana, text= "Añadir producto")

# Definir campos de pantalla (INFO)
info_label = Label(ventana, text= "Información del producto")
data_label = Label(ventana, text= "Creado por Javier Checa - 2026")


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
