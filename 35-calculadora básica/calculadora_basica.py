import tkinter as tk
from tkinter import messagebox
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("340x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.memoria = 0.0
        self.expresion = ""

        # Pantalla de visualización
        self.pantalla = tk.Entry(
            root, 
            font=("Consolas", 24), 
            bg="#181825", 
            fg="#1de53b", 
            bd=0, 
            justify="right", 
            insertbackground="#cdd6f4"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=15, sticky="nsew")

        # Botones de la calculadora
        botones = [
            ('MC', 1, 0), ('MR', 1, 1), ('M+', 1, 2), ('M-', 1, 3),
            ('C', 2, 0),  ('√', 2, 1),  ('%', 2, 2),  ('÷', 2, 3),
            ('7', 3, 0),  ('8', 3, 1),  ('9', 3, 2),  ('×', 3, 3),
            ('4', 4, 0),  ('5', 4, 1),  ('6', 4, 2),  ('-', 4, 3),
            ('1', 5, 0),  ('2', 5, 1),  ('3', 5, 2),  ('+', 5, 3),
            ('±', 6, 0),  ('0', 6, 1),  ('.', 6, 2),  ('=', 6, 3)
        ]

        # Configuración del grid
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

        # Crear botones con estilos
        for (texto, fila, columna) in botones:
            bg_color = "#5BB7F1"
            fg_color = "#ecf2f3"
            
            if texto in ['MC', 'MR', 'M+', 'M-']:
                bg_color = "#020a4d"
            elif texto in ['C', '√', '%', '÷', '×', '-', '+', '±']:
                bg_color = "#EE9A12"
                fg_color = "#dbdea1"
            elif texto == '=':
                bg_color = "#dc1111"
                fg_color = "#e4e4ee"

            btn = tk.Button(
                root, 
                text=texto, 
                font=("Segoe UI", 14, "bold"),
                bg=bg_color, 
                fg=fg_color, 
                activebackground="#585b70",
                activeforeground="#ffffff",
                bd=0, 
                relief="flat",
                command=lambda t=texto: self.on_button_click(t)
            )
            btn.grid(row=fila, column=columna, padx=3, pady=3, sticky="nsew")

    def obtener_valor_actual(self):
        try:
            val = float(self.pantalla.get())
            return val
        except ValueError:
            return None

    def actualizar_pantalla(self, valor):
        self.pantalla.delete(0, tk.END)
        # Mostrar entero si no tiene parte decimal
        if isinstance(valor, float) and valor.is_integer():
            valor = int(valor)
        self.pantalla.insert(0, str(valor))

    def on_button_click(self, char):
        texto_actual = self.pantalla.get()

        # Operaciones de Memoria
        if char == 'MC':
            self.memoria = 0.0
        elif char == 'MR':
            self.actualizar_pantalla(self.memoria)
        elif char == 'M+':
            val = self.obtener_valor_actual()
            if val is not None:
                self.memoria += val
        elif char == 'M-':
            val = self.obtener_valor_actual()
            if val is not None:
                self.memoria -= val

        # Limpiar y Edición
        elif char == 'C':
            self.pantalla.delete(0, tk.END)
        elif char == '±':
            val = self.obtener_valor_actual()
            if val is not None:
                self.actualizar_pantalla(-val)

        # Raíz Cuadrada
        elif char == '√':
            val = self.obtener_valor_actual()
            if val is not None:
                if val < 0:
                    messagebox.showerror("Error", "No se puede calcular la raíz cuadrada de un número negativo.")
                else:
                    self.actualizar_pantalla(math.sqrt(val))

        # Porcentaje (Convierte el valor actual en su fracción decimal / 100)
        elif char == '%':
            val = self.obtener_valor_actual()
            if val is not None:
                self.actualizar_pantalla(val / 100)

        # Operadores Aritméticos Básicos
        elif char in ['+', '-', '×', '÷']:
            if texto_actual and texto_actual[-1] not in ['+', '-', '*', '/']:
                op_map = {'×': '*', '÷': '/'}
                self.pantalla.insert(tk.END, op_map.get(char, char))

        # Calcular Resultado (=)
        elif char == '=':
            try:
                expresion = texto_actual.replace('×', '*').replace('÷', '/')
                resultado = eval(expresion)
                self.actualizar_pantalla(resultado)
            except ZeroDivisionError:
                messagebox.showerror("Error", "División por cero no permitida.")
            except Exception:
                messagebox.showerror("Error", "Expresión inválida.")

        # Entradas numéricas y punto decimal
        else:
            self.pantalla.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()