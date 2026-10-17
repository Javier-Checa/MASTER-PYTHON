from tkinter import *
ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("800x800")


marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue",
    bd=10,
    relief="raised"
)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES)


marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=8,
    relief="ridge"
)
marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="lightgreen",
    bd=12,
    relief="sunken"
)
marco.pack(side=BOTTOM, anchor=W)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="orange",
    bd=10,
    relief="raised"
)
marco_padre.pack(side=TOP, fill=X, expand=YES)


ventana.mainloop()