from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Javier Checa")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Javier Checa")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.pack(side=LEFT, anchor=NW, fill=X, expand=YES)

# Campo de texto
campo_texto = Entry(ventana)
campo_texto.pack()

ventana.mainloop()