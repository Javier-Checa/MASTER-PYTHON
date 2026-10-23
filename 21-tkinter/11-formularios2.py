from tkinter import *

ventana = Tk()
ventana.title("Formularios 2")
ventana.geometry("800x500")


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

def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu género?"). grid(row=5)

Radiobutton(
    ventana,
    text="Masculino",
    value="MACHOTE",
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana, 
    text="Femenino",
    value="MARIQUILLA",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)



# Option menu
def seleccionar():
    seleccionado.config(text=choose.get())

choose = StringVar()
choose.set("Opción 1")

Label(ventana, text="Selecciona una opción:").grid(row=5, column=1)

select = OptionMenu(ventana, choose, "Opción 1", "Opción 2", "Opción 3")
select.grid(row=6, column=1)

Button(ventana, text=("Ver la opción"), command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()