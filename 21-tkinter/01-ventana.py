# Tkinter es un módulo de Python que se utiliza para crear interfaces gráficas de usuario (GUI). 
# A continuación, se muestra un ejemplo básico de cómo crear una ventana utilizando Tkinter:

from tkinter import *
import os.path

# Crear la ventana principal o raíz

ventana = Tk()

# Título de la ventana
ventana.title("Mi primera interfaz gráfica con Python y la librería Tkinter")

# Comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/logotipo.ico')

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./21-tkinter/imagenes/logotipo.ico')

# Icono de la ventana
ventana.iconbitmap(ruta_icono)

# Mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()

# Cambiar el color de fondo de la ventana
ventana.config(bg="lightyellow")


# Cambio en el tamaño de la ventana
ventana.geometry("750x450")  # Ancho x Alto

# Bloquear el cambio de tamaño del alto de la ventana
ventana.resizable(True, False)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()