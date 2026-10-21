"""
CALCULADORA:
-   Dos campos de texto
-   4 botones para las operaciones
-   Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("EJERCICIO COMPLETO CON TKINTER")
ventana.geometry("400x400")
ventana.config(bd=25)


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=GROOVE  
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1).pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar +").pack(side="left")
Button(marco, text="Restar -").pack(side="left")
Button(marco, text="Multiplicar x").pack(side="left")
Button(marco, text="Dividir /").pack(side="left")


ventana.mainloop()