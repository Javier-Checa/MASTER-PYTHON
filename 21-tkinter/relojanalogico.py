import math
import tkinter as tk
from datetime import datetime


class RelojAnalogico:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Reloj analógico")
        self.ventana.geometry("460x500")
        self.ventana.minsize(320, 360)
        self.ventana.configure(bg="#1e1e1e")

        self.lienzo = tk.Canvas(
            ventana,
            bg="#07032f",
            highlightthickness=0,
        )
        self.lienzo.pack(fill="both", expand=True, padx=16, pady=(16, 4))
        self.etiqueta_fecha = tk.Label(
            ventana,
            font=("Segoe UI", 11),
            bg="#1e1e1e",
            fg="#b0b0b0",
        )
        self.etiqueta_fecha.pack(pady=(0, 14))

        self.lienzo.bind("<Configure>", self.dibujar)
        self.actualizar()

    def dibujar(self, _evento=None):
        ancho = self.lienzo.winfo_width()
        alto = self.lienzo.winfo_height()
        tamano = min(ancho, alto) - 20
        if tamano <= 0:
            return

        centro_x = ancho / 2
        centro_y = alto / 2
        radio = tamano / 2
        self.lienzo.delete("all")
        self.lienzo.create_oval(
            centro_x - radio,
            centro_y - radio,
            centro_x + radio,
            centro_y + radio,
            fill="#282828",
            outline="#00c9a7",
            width=3,
        )

        for marca in range(60):
            angulo = math.radians(marca * 6 - 90)
            es_hora = marca % 5 == 0
            radio_exterior = radio * 0.91
            radio_interior = radio * (0.80 if es_hora else 0.86)
            x1 = centro_x + math.cos(angulo) * radio_interior
            y1 = centro_y + math.sin(angulo) * radio_interior
            x2 = centro_x + math.cos(angulo) * radio_exterior
            y2 = centro_y + math.sin(angulo) * radio_exterior
            self.lienzo.create_line(
                x1,
                y1,
                x2,
                y2,
                fill="#eeeeee" if es_hora else "#777777",
                width=max(1, round(radio * (0.018 if es_hora else 0.007))),
                capstyle=tk.ROUND,
            )

        for hora in range(1, 13):
            angulo = math.radians(hora * 30 - 90)
            distancia = radio * 0.68
            x = centro_x + math.cos(angulo) * distancia
            y = centro_y + math.sin(angulo) * distancia
            self.lienzo.create_text(
                x,
                y,
                text=str(hora),
                fill="#eeeeee",
                font=("Segoe UI", max(9, round(radio * 0.11)), "bold"),
            )

        ahora = datetime.now()
        segundos = ahora.second + ahora.microsecond / 1_000_000
        minutos = ahora.minute + segundos / 60
        horas = (ahora.hour % 12) + minutos / 60
        self._dibujar_aguja(centro_x, centro_y, radio * 0.48, horas * 30 - 90, "#eeeeee", max(3, round(radio * 0.035)))
        self._dibujar_aguja(centro_x, centro_y, radio * 0.68, minutos * 6 - 90, "#00c9a7", max(2, round(radio * 0.022)))
        self._dibujar_aguja(centro_x, centro_y, radio * 0.76, segundos * 6 - 90, "#ff6b6b", max(1, round(radio * 0.009)))
        self.lienzo.create_oval(
            centro_x - radio * 0.035,
            centro_y - radio * 0.035,
            centro_x + radio * 0.035,
            centro_y + radio * 0.035,
            fill="#ff6b6b",
            outline="",
        )

    def _dibujar_aguja(self, centro_x, centro_y, longitud, angulo_grados, color, grosor):
        angulo = math.radians(angulo_grados)
        extremo_x = centro_x + math.cos(angulo) * longitud
        extremo_y = centro_y + math.sin(angulo) * longitud
        self.lienzo.create_line(
            centro_x,
            centro_y,
            extremo_x,
            extremo_y,
            fill=color,
            width=grosor,
            capstyle=tk.ROUND,
        )

    def actualizar(self):
        self.etiqueta_fecha.config(text=datetime.now().strftime("%d/%m/%Y"))
        self.dibujar()
        self.ventana.after(1000, self.actualizar)


if __name__ == "__main__":
    ventana = tk.Tk()
    RelojAnalogico(ventana)
    ventana.mainloop()
