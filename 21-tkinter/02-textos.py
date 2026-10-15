from tkinter import *

ventana = Tk()
ventana.title("Ventana para Ejemplo de Textos")
ventana.geometry("600x600")

texto = Label(ventana, text="Hola, este es mi texto. Bienvenido a mi programa!")
texto.config(
    font=("Arial", 18, "bold"), 
    fg="white", 
    bg="darkgray",
    padx=650,
    pady=45
    )
texto.pack()


texto = Label(ventana, text="Soy Javier Checa, tu programador amigo.")
texto.config(font=("Times", 16, "italic"),
             fg="darkblue", 
             bg="orange", 
             padx=25, 
             pady=25, 
             height=12, 
             width=60, 
             cursor="hand2"
)
texto.pack(anchor=SE)


def pruebas(nombre, apellidos, pais):
    return f"Hola, {nombre} {apellidos}, veo que eres de {pais}."




texto = Label(ventana, text=pruebas(pais="España", nombre="Javier", apellidos="Checa")) # Introducción aleatoria de parámetros en la función pruebas. Se puede hacer de esta manera, o bien, de la manera tradicional, es decir, pruebas("Javier", "Checa", "España").
texto.config(font=("Consolas", 16, "bold"),
             fg="darkgreen", 
             bg="lightgreen", 
             padx=25, 
             pady=25, 
             height=12, 
             width=60, 
             cursor="circle"
)
texto.pack(anchor=SW)



ventana.mainloop()
