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
def mostrarProfesion():
    texto = ""
    
    if web.get():
        texto += "Desarrollo web"
 
    if movil.get():
        if web.get():
            texto += " y desarrollo móvil"  
        else:
            texto += "Desarrollo móvil"
        
        
    mostrar.config(
        text=texto,
        bg="green",
        fg="yellow"
    )
     
web = IntVar()
movil = IntVar()

Label(ventana, text="¿A qué te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="Desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="Desarrollo móvil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons
Radiobutton(ventana, text="Masculino").grid(row=5)
Radiobutton(ventana, text="Femenino").grid(row=6)


# Option menu



ventana.mainloop()