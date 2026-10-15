from tkinter import *

ventana = Tk()
ventana.title("Ventana para Ejemplo de Textos")
ventana.geometry("500x500")

texto = Label(ventana, text="Hola, este es mi texto. Bienvenido a mi programa!", font=("Arial", 14))
texto.pack()


texto = Label(ventana, text="Soy Javier Checa, tu programador amigo.", font=("Arial", 14))
texto.pack()




ventana.mainloop()
