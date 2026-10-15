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


texto = Label(ventana, text="Este es un curso de Python.")
texto.config(font=("Consolas", 16, "bold"),
             fg="yellow", 
             bg="red", 
             padx=25, 
             pady=25, 
             height=12, 
             width=60, 
             cursor="circle"
)
texto.pack(anchor=SW)



ventana.mainloop()
