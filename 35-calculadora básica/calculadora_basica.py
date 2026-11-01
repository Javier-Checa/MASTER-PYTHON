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
            fg="#cdd6f4", 
            bd=0, 
            justify="right", 
            insertbackground="#cdd6f4"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=15, sticky="nsew")        