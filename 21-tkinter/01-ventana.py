# Tkinter es un módulo de Python que se utiliza para crear interfaces gráficas de usuario (GUI). 
# A continuación, se muestra un ejemplo básico de cómo crear una ventana utilizando Tkinter:

from tkinter import *

# Crear la ventana principal o raíz

ventana = Tk()

# Cambio en el tamaño de la ventana
ventana.geometry("750x450")  # Ancho x Alto

# Bloquear el cambio de tamaño del alto de la ventana
ventana.resizable(True, False)

# Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()