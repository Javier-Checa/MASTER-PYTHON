from tkinter import *
ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("750x750")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="orange",
    bd=10,
    relief="raised"
)
marco.pack(side=LEFT, anchor=SW)


marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="yellow",
    bd=8,
    relief="ridge"
)
marco.pack(side=RIGHT, anchor=SE)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bg="lightgreen",
    bd=12,
    relief="sunken"
)
marco.pack(side=BOTTOM, anchor=S)


ventana.mainloop()