from tkinter import *

ventana = Tk()
ventana.title("Formularios 2")
ventana.geometry("500x400")


encabezado = Label(ventana, text="Formularios avanzados")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 18)
)
encabezado.pack(anchor=CENTER, side=TOP, fill=X)

ventana.mainloop()