

import math
import tkinter as tk
from tkinter import messagebox


class Notas:
    """Clase encargada de la lógica matemática y cálculos estadísticos de las 5 notas."""

    def __init__(self, lista_notas: list[float]):
        if len(lista_notas) != 5:
            raise ValueError("Se requieren exactamente 5 notas.")
        self.lista_notas = lista_notas

    def calcular_promedio(self) -> float:
        """Calcula el promedio (media aritmética) de las notas."""
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self) -> float:
        """Calcula la desviación estándar poblacional de las notas."""
        promedio = self.calcular_promedio()
        suma_cuadrados = sum((x - promedio) ** 2 for x in self.lista_notas)
        varianza = suma_cuadrados / len(self.lista_notas)
        return math.sqrt(varianza)

    def calcular_mayor(self) -> float:
        """Obtiene la mayor nota ingresada."""
        return max(self.lista_notas)

    def calcular_menor(self) -> float:
        """Obtiene la menor nota ingresada."""
        return min(self.lista_notas)


class VentanaPrincipal(tk.Tk):
    """Clase que representa la interfaz gráfica de usuario en Tkinter."""

    def __init__(self):
        super().__init__()
        self.title("Cálculo de Notas")
        self.geometry("340x420")
        self.resizable(False, False)

        self.entries_notas = []
        self.crear_widgets()

    def crear_widgets(self):
        # Campos de entrada para las 5 notas
        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i + 1}:")
            lbl.place(x=40, y=20 + (i * 35))

            entry = tk.Entry(self, width=15)
            entry.place(x=130, y=20 + (i * 35))
            self.entries_notas.append(entry)

        # Botón Calcular
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.place(x=50, y=200, width=100)

        # Botón Limpiar
        btn_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        btn_limpiar.place(x=180, y=200, width=100)

        # Etiquetas para los resultados en la parte inferior
        self.lbl_promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.lbl_promedio.place(x=40, y=250, width=260)

        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ", anchor="w")
        self.lbl_desviacion.place(x=40, y=280, width=260)

        self.lbl_mayor = tk.Label(self, text="Mayor nota = ", anchor="w")
        self.lbl_mayor.place(x=40, y=310, width=260)

        self.lbl_menor = tk.Label(self, text="Menor nota = ", anchor="w")
        self.lbl_menor.place(x=40, y=340, width=260)

    def calcular(self):
        """Lee los valores, realiza las validaciones y actualiza las etiquetas."""
        try:
            valores = []
            for entry in self.entries_notas:
                texto = entry.get().strip()
                if not texto:
                    raise ValueError("Campo vacío")
                valor = float(texto)
                valores.append(valor)

            # Instancia la lógica de negocio
            notas_obj = Notas(valores)

            # Actualiza resultados en pantalla
            self.lbl_promedio.config(
                text=f"Promedio = {notas_obj.calcular_promedio():.2f}"
            )
            self.lbl_desviacion.config(
                text=f"Desviación estándar = {notas_obj.calcular_desviacion():.2f}"
            )
            self.lbl_mayor.config(
                text=f"Mayor nota = {notas_obj.calcular_mayor():.2f}"
            )
            self.lbl_menor.config(
                text=f"Menor nota = {notas_obj.calcular_menor():.2f}"
            )

        except ValueError:
            messagebox.showerror(
                "Error de ingreso",
                "Por favor ingrese valores numéricos válidos en los 5 campos.",
            )

    def limpiar(self):
        """Limpia las cajas de texto y las etiquetas de resultados."""
        for entry in self.entries_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Mayor nota = ")
        self.lbl_menor.config(text="Menor nota = ")


def main():
    app = VentanaPrincipal()
    app.mainloop()


if __name__ == "__main__":
    main()
