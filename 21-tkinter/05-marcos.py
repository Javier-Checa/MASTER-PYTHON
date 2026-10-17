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
marco.pack(side=LEFT, anchor=SW)


marco = Frame(ventana, width=350, height=250)
marco.config(
    bg="yellow",
    bd=8,
    relief="ridge"
)
marco.pack(side=RIGHT, anchor=NE)


ventana.mainloop()