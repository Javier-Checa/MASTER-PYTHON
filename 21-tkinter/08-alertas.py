from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Ventana para alertas | Javier Checa")
ventana.geometry("700x500")
ventana.config(bd=50)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola, soy Triki, ¡¡¡el mostruo de la galletas!!!")


Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()


ventana.mainloop()
