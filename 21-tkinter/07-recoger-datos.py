from tkinter import *

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
    bg="#ccc"
)


def getDato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Introduce un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
Label(ventana, textvariable=resultado).pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)


ventana.mainloop()
