import math
import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod

# --- Jerarquía de Clases POO ---

class FiguraGeometrica(ABC):
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    @property
    def volumen(self):
        return self._volumen

    @property
    def superficie(self):
        return self._superficie

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        return (2 * math.pi * self.radio * self.altura) + (2 * math.pi * (self.radio ** 2))


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self._volumen = self.calcular_volumen()
        self._superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (1.0 / 3.0) * (self.base ** 2) * self.altura

    def calcular_superficie(self):
        return (self.base ** 2) + (2 * self.base * self.apotema)


# --- Interfaz Gráfica con Pestañas ---

class VentanaFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.3 - Cálculo de Figuras Geométricas")
        self.geometry("420x280")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        tab_cilindro = ttk.Frame(notebook)
        tab_esfera = ttk.Frame(notebook)
        tab_piramide = ttk.Frame(notebook)

        notebook.add(tab_cilindro, text="Cilindro")
        notebook.add(tab_esfera, text="Esfera")
        notebook.add(tab_piramide, text="Pirámide")

        self.crear_tab_cilindro(tab_cilindro)
        self.crear_tab_esfera(tab_esfera)
        self.crear_tab_piramide(tab_piramide)

    def crear_tab_cilindro(self, parent):
        tk.Label(parent, text="Radio (cm):").place(x=20, y=20)
        txt_radio = tk.Entry(parent)
        txt_radio.place(x=130, y=20, width=120)

        tk.Label(parent, text="Altura (cm):").place(x=20, y=55)
        txt_altura = tk.Entry(parent)
        txt_altura.place(x=130, y=55, width=120)

        lbl_vol = tk.Label(parent, text="Volumen (cm³): -", font=("Arial", 10, "bold"))
        lbl_vol.place(x=20, y=110)

        lbl_sup = tk.Label(parent, text="Superficie (cm²): -", font=("Arial", 10, "bold"))
        lbl_sup.place(x=20, y=140)

        def calcular():
            try:
                r = float(txt_radio.get())
                h = float(txt_altura.get())
                cil = Cilindro(r, h)
                lbl_vol.config(text=f"Volumen (cm³): {cil.volumen:.2f}")
                lbl_sup.config(text=f"Superficie (cm²): {cil.superficie:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

        btn = tk.Button(parent, text="Calcular", command=calcular)
        btn.place(x=270, y=35, width=110, height=35)

    def crear_tab_esfera(self, parent):
        tk.Label(parent, text="Radio (cm):").place(x=20, y=20)
        txt_radio = tk.Entry(parent)
        txt_radio.place(x=130, y=20, width=120)

        lbl_vol = tk.Label(parent, text="Volumen (cm³): -", font=("Arial", 10, "bold"))
        lbl_vol.place(x=20, y=80)

        lbl_sup = tk.Label(parent, text="Superficie (cm²): -", font=("Arial", 10, "bold"))
        lbl_sup.place(x=20, y=110)

        def calcular():
            try:
                r = float(txt_radio.get())
                esf = Esfera(r)
                lbl_vol.config(text=f"Volumen (cm³): {esf.volumen:.2f}")
                lbl_sup.config(text=f"Superficie (cm²): {esf.superficie:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese un valor numérico válido.")

        btn = tk.Button(parent, text="Calcular", command=calcular)
        btn.place(x=270, y=20, width=110, height=35)

    def crear_tab_piramide(self, parent):
        tk.Label(parent, text="Base (cm):").place(x=20, y=20)
        txt_base = tk.Entry(parent)
        txt_base.place(x=130, y=20, width=120)

        tk.Label(parent, text="Altura (cm):").place(x=20, y=55)
        txt_altura = tk.Entry(parent)
        txt_altura.place(x=130, y=55, width=120)

        tk.Label(parent, text="Apotema (cm):").place(x=20, y=90)
        txt_apotema = tk.Entry(parent)
        txt_apotema.place(x=130, y=90, width=120)

        lbl_vol = tk.Label(parent, text="Volumen (cm³): -", font=("Arial", 10, "bold"))
        lbl_vol.place(x=20, y=135)

        lbl_sup = tk.Label(parent, text="Superficie (cm²): -", font=("Arial", 10, "bold"))
        lbl_sup.place(x=20, y=165)

        def calcular():
            try:
                b = float(txt_base.get())
                h = float(txt_altura.get())
                a = float(txt_apotema.get())
                pir = Piramide(b, h, a)
                lbl_vol.config(text=f"Volumen (cm³): {pir.volumen:.2f}")
                lbl_sup.config(text=f"Superficie (cm²): {pir.superficie:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

        btn = tk.Button(parent, text="Calcular", command=calcular)
        btn.place(x=270, y=55, width=110, height=35)


if __name__ == "__main__":
    app = VentanaFiguras()
    app.mainloop()
