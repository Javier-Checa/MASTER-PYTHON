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
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# Botones check
Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(ventana, text="Desarrollo web").grid(row=2, column=0)
Checkbutton(ventana, text="Desarrollo móvil").grid(row=3, column=0)

# Radio buttons

# Option menu



ventana.mainloop()