from tkinter import *

ventana = Tk()
ventana.title("MENÚS DESPLEGABLES CON TKINTER")
ventana.geometry("900x600")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_command(label="Guardar")
archivo.add_separator()
archivo.add_command(label="Previsualizar")
archivo.add_command(label="Imprimir")

editar = Menu(mi_menu)
editar.add_command(label="Copiar")
editar.add_command(label="Cortar")
editar.add_command(label="Pegar")

ayuda = Menu(mi_menu)
ayuda.add_command(label="Sobre este programa")

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_cascade(label="Editar", menu=editar)
mi_menu.add_command(label="Selección")
mi_menu.add_command(label="Ver")
mi_menu.add_command(label="Ir a")
mi_menu.add_cascade(label="Ayuda", menu=ayuda)


ventana.mainloop()

