from tkinter import *

ventana = Tk()
ventana.title("Ventana para Ejemplo de Textos")
ventana.geometry("600x600")

texto = Label(ventana, text="Hola, este es mi texto. Bienvenido a mi programa!")
texto.config(
    font=("Arial", 16), 
    fg="white", 
    bg="darkgray",
    padx=25,
    pady=25
    )
texto.pack()


texto = Label(ventana, text="Soy Javier Checa, tu programador amigo.")
texto.config(font=("Arial", 14), fg="darkblue", bg="lightgray", padx=25, pady=25)
texto.pack()




ventana.mainloop()
