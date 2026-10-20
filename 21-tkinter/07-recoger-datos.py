from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
    bg="#ccc"
)

Label(ventana, text="Mete un texto").pack()

ventana.mainloop()
