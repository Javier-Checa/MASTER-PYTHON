"""
Crear un progrma que tenga:
- (hecho) - Ventana
- (hecho) - Tamaño fijo de la ventana
- (hecho) - No redimensionable
- (hecho) - Un menú
- (hecho) - Opción de salir 
- (hecho) - Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente sin usar una base de datos
- Mostrar los datos listados en la pantalla principal o home (landing)

"""
from tkinter import *


# Definir ventana
ventana = Tk()
ventana.geometry("600x600")
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0, 0)

# Pantallas

def home():
# Mostrar pantalla    
    
    home_label.config(
        fg= "white",
        bg= "black",
        font=("Arial", 30),
        padx=125,
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
        padx=140,
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
        padx=180,
        pady=20
        
    )
    info_label.grid(row=0, column=0)
    
    data_label.grid(row=1, column=0)
    
    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    
    return True

# Variables importantes
name_data = StringVar()
price_data = StringVar()


# Definir campos de pantalla (INCIO)
home_label = Label(ventana, text= "Pantalla de inicio")

# Definir campos de pantalla (ADD)
add_label = Label(ventana, text= "Añadir producto")

# Campos del formulario
add_name_label = Label(ventana, text="Nombre del producto")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio del producto")
add_price_entry = Entry(ventana, textvariable=price_data)



# Definir campos de pantalla (INFO)
info_label = Label(ventana, text= "Información")
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
