import tkinter as tk
from time import strftime

def actualizar_reloj():
    # Obtener la hora y la fecha actual del sistema
    tiempo_actual = strftime('%H:%M:%S')
    fecha_actual = strftime('%A, %d de %B de %Y')
    
    # Actualizar los textos de las etiquetas
    lbl_hora.config(text=tiempo_actual)
    lbl_fecha.config(text=fecha_actual)
    
    # Programar la función para que se vuelva a ejecutar en 1000 ms (1 segundo)
    lbl_hora.after(1000, actualizar_reloj)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Reloj Digital")
root.geometry("450x200")
root.minsize(400, 180)
root.config(bg="#1e1e1e")  # Fondo oscuro elegante

# Estilo y etiqueta para la Hora
lbl_hora = tk.Label(
    root, 
    font=('Segoe UI', 48, 'bold'), 
    background='#1e1e1e', 
    foreground='#00ffcc'
)
lbl_hora.pack(anchor='center', pady=(30, 5))

# Estilo y etiqueta para la Fecha
lbl_fecha = tk.Label(
    root, 
    font=('Segoe UI', 13), 
    background='#1e1e1e', 
    foreground='#b0b0b0'
)
lbl_fecha.pack(anchor='center')

# Iniciar la actualización del reloj
actualizar_reloj()

# Mantener la ventana abierta en ejecución
root.mainloop()