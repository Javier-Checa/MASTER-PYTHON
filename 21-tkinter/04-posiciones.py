from tkinter import *

ventana = Tk()
ventana.title("Ventana para Ejemplo de Textos")
# ventana.geometry("600x600")

texto = Label(ventana, text="¡Bienvenido a mi programa!")
texto.config(
    font=("Arial", 18, "bold"), 
    fg="white", 
    bg="darkgray",
    padx=650,
    pady=45
    )
texto.pack(side=TOP, fill=X)


texto = Label(ventana, text="Soy Javier Checa")
texto.config(font=("Times", 14, "bold italic"),
             fg="darkblue", 
             bg="orange", 
             padx=5, 
             pady=5, 
             height=5, 
             width=20, 
             cursor="hand2"
)
texto.pack(side=TOP, fill=X, expand=True)


texto = Label(ventana, text=("Texto básico 1"))
texto.config(font=("Consolas", 14, "bold"),
             fg="darkgreen", 
             bg="lightgreen", 
             padx=5, 
             pady=5, 
             height=5, 
             width=20, 
             cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=("Texto básico 2"))
texto.config(font=("Consolas", 14, "bold"),
             fg="darkgreen", 
             bg="lightblue", 
             padx=5, 
             pady=5, 
             height=5, 
             width=20, 
             cursor="arrow"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=("Texto básico 3"))
texto.config(font=("Consolas", 14, "bold"),
             fg="darkgreen", 
             bg="pink", 
             padx=5, 
             pady=5, 
             height=5, 
             width=20, 
             cursor="circle"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text=("Texto básico 4"))
texto.config(font=("Consolas", 14, "bold"),
             fg="darkgreen", 
             bg="lightyellow", 
             padx=5, 
             pady=5, 
             height=5, 
             width=20, 
             cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()
