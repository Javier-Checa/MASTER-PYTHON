import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya (Tic Tac Toe)")
        self.root.resizable(False, False)

        self.turno = "X"
        self.tablero = [""] * 9
        self.botones = []

        # Etiqueta de estado
        self.label_estado = tk.Label(
            root, text="Turno del jugador: X", font=("Arial", 14)
        )
        self.label_estado.pack(pady=10)

        # Marco para el tablero
        self.frame_tablero = tk.Frame(root)
        self.frame_tablero.pack()

        # Crear los 9 botones de la cuadrícula
        self.crear_tablero()
        
        # Botón para reiniciar
        self.btn_reiniciar = tk.Button(
            root,
            text="Reiniciar Juego",
            font=("Arial", 12),
            command=self.reiniciar_juego,
        )
        self.btn_reiniciar.pack(pady=10)
        
    def crear_tablero(self):
        for i in range(9):
            fila = i // 3
            columna = i % 3
            btn = tk.Button(
                self.frame_tablero,
                text="",
                font=("Arial", 24, "bold"),
                width=5,
                height=2,
                command=lambda idx=i: self.presionar_boton(idx),
            )
            btn.grid(row=fila, column=columna, padx=2, pady=2)
            self.botones.append(btn)
            
    
        