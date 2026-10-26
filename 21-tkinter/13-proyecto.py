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
    add_frame.grid_remove()   
    
    return True

def add():
    # Encabezado
    add_label.config(
        fg= "white",
        bg= "green",
        font=("Arial", 30),
        padx=140,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    
    # Campos del formulario
    add_frame.grid(row=1)
      
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    add_separator.grid(row=5, column=1)
    
    boton.grid(row=6, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )
    
    
    
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
    add_frame.grid_remove()
    
    return True

# Variables importantes
name_data = StringVar()
price_data = StringVar()


# Definir campos de pantalla (INCIO)
home_label = Label(ventana, text= "Pantalla de inicio")

# Definir campos de pantalla (ADD)
add_label = Label(ventana, text= "Añadir producto")

# Campos del formulario
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar")



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
