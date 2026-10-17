from tkinter import *
ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x400")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="orange",
    bd=10,
    relief="raised"
)

marco.pack()

ventana.mainloop()