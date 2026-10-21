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
ventana.geometry("700x400")
ventana.config(bd=25)


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


Label(ventana, text="Primer número: ").pack()
Entry(ventana, textvariable=numero1).pack()

Label(ventana, text="Segundo número: ").pack()
Entry(ventana, textvariable=numero2).pack()






ventana.mainloop()