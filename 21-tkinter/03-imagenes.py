from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")



Label(ventana, text="La gatita presumida", font=("Arial", 14)).pack(anchor=W)

imagen = Image.open("./21-tkinter/imagenes/la_gatita_presumida.jpg")    
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()
