import tkinter as tk
from time import strftime

class RelojDigitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj Digital")
        self.root.geometry("500x250")
        self.root.minsize(250, 120)
        self.root.config(bg="#1e1e1e")

        # Estado para la opción "siempre encima"
        self.siempre_encima = False

        # Frame superior para el botón de control
        frame_top = tk.Frame(root, bg="#1e1e1e")
        frame_top.pack(fill='x', padx=10, pady=(10, 0))

        # Botón para mantener siempre encima
        self.btn_topmost = tk.Button(
            frame_top,
            text="📌 Fijar encima: OFF",
            command=self.toggle_siempre_encima,
            font=('Segoe UI', 9, 'bold'),
            bg="#333333",
            fg="#ffffff",
            activebackground="#444444",
            activeforeground="#ffffff",
            bd=0,
            padx=10,
            pady=4,
            cursor="hand2"
        )
        self.btn_topmost.pack(anchor='ne')

        # Etiqueta para la Hora
        self.lbl_hora = tk.Label(
            root,
            font=('Segoe UI', 40, 'bold'),
            bg='#1e1e1e',
            fg='#00ffcc'
        )
        self.lbl_hora.pack(expand=True, fill='both')

        # Etiqueta para la Fecha
        self.lbl_fecha = tk.Label(
            root,
            font=('Segoe UI', 12),
            bg='#1e1e1e',
            fg='#b0b0b0'
        )
        self.lbl_fecha.pack(fill='x', pady=(0, 15))

        # Vincular evento de redimensionado de ventana
        self.root.bind('<Configure>', self.al_redimensionar)

        # Iniciar reloj
        self.actualizar_reloj()

    def toggle_siempre_encima(self):
        # Cambiar estado
        self.siempre_encima = not self.siempre_encima
        # Aplicar propiedad de mantener encima en Windows/Tkinter
        self.root.attributes('-topmost', self.siempre_encima)
        
        # Actualizar apariencia del botón
        if self.siempre_encima:
            self.btn_topmost.config(
                text="📌 Fijar encima: ON",
                bg="#007acc",
                fg="#ffffff"
            )
        else:
            self.btn_topmost.config(
                text="📌 Fijar encima: OFF",
                bg="#333333",
                fg="#ffffff"
            )

    def al_redimensionar(self, event):
        # Ajustar fuente solo si el evento proviene de la ventana principal
        if event.widget == self.root:
            ancho = event.width
            alto = event.height

            # Calcular tamaño de fuente proporcional
            tamano_hora = max(16, int(min(ancho / 7, alto / 3)))
            tamano_fecha = max(9, int(tamano_hora / 3.2))

            # Actualizar fuentes
            self.lbl_hora.config(font=('Segoe UI', tamano_hora, 'bold'))
            self.lbl_fecha.config(font=('Segoe UI', tamano_fecha))

    def actualizar_reloj(self):
        # Obtener tiempo y fecha actual
        tiempo_actual = strftime('%H:%M:%S')
        fecha_actual = strftime('%A, %d de %B de %Y')

        self.lbl_hora.config(text=tiempo_actual)
        self.lbl_fecha.config(text=fecha_actual)

        # Programar siguiente actualización en 1 segundo
        self.lbl_hora.after(1000, self.actualizar_reloj)


if __name__ == "__main__":
    root = tk.Tk()
    app = RelojDigitalApp(root)
    root.mainloop()