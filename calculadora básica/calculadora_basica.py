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
        
        