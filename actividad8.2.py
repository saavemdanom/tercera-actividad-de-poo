import tkinter as tk
from tkinter import messagebox, ttk

class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre.strip()
        self.apellidos = apellidos.strip()
        self.telefono = telefono.strip()
        self.direccion = direccion.strip()

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - Tel: {self.telefono} - Dir: {self.direccion}"


class VentanaPersonas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 8.2 - Gestión de Personas")
        self.geometry("520x480")
        self.resizable(False, False)

        self.personas = []
        self.indice_edicion = None

        self.crear_interface()

    def crear_interface(self):
        # Etiquetas y Campos de entrada
        tk.Label(self, text="Nombre:").place(x=20, y=20)
        self.txt_nombre = tk.Entry(self)
        self.txt_nombre.place(x=120, y=20, width=160)

        tk.Label(self, text="Apellidos:").place(x=20, y=55)
        self.txt_apellidos = tk.Entry(self)
        self.txt_apellidos.place(x=120, y=55, width=160)

        tk.Label(self, text="Teléfono:").place(x=20, y=90)
        self.txt_telefono = tk.Entry(self)
        self.txt_telefono.place(x=120, y=90, width=160)

        tk.Label(self, text="Dirección:").place(x=20, y=125)
        self.txt_direccion = tk.Entry(self)
        self.txt_direccion.place(x=120, y=125, width=160)

        # Botones
        self.btn_anadir = tk.Button(self, text="Añadir", command=self.anadir_persona)
        self.btn_anadir.place(x=310, y=20, width=180)

        self.btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_persona)
        self.btn_eliminar.place(x=310, y=55, width=180)

        self.btn_editar = tk.Button(self, text="Editar Seleccionado", command=self.cargar_para_editar)
        self.btn_editar.place(x=310, y=90, width=180)

        self.btn_guardar = tk.Button(self, text="Guardar Cambios", command=self.guardar_cambios, state=tk.DISABLED)
        self.btn_guardar.place(x=310, y=125, width=180)

        self.btn_limpiar = tk.Button(self, text="Limpiar Lista", command=self.limpiar_lista)
        self.btn_limpiar.place(x=310, y=160, width=180)

        # Listbox con Barra de Desplazamiento
        frame_lista = tk.Frame(self)
        frame_lista.place(x=20, y=200, width=470, height=250)

        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

    def existe_duplicado(self, nombre, apellidos, indice_ignorado=None):
        for i, p in enumerate(self.personas):
            if i == indice_ignorado:
                continue
            if p.nombre.lower() == nombre.lower() and p.apellidos.lower() == apellidos.lower():
                return True
        return False

    def anadir_persona(self):
        nom = self.txt_nombre.get().strip()
        ape = self.txt_apellidos.get().strip()
        tel = self.txt_telefono.get().strip()
        dir_p = self.txt_direccion.get().strip()

        if not nom or not ape:
            messagebox.showerror("Error", "Debe ingresar al menos Nombre y Apellidos.")
            return

        # Validación de duplicados
        if self.existe_duplicado(nom, ape):
            messagebox.showwarning("Registro Duplicado", "¡Alerta! Ya existe una persona con ese nombre y apellidos en la lista.")
            return

        p = Persona(nom, ape, tel, dir_p)
        self.personas.append(p)
        self.actualizar_listbox()
        self.limpiar_campos()

    def eliminar_persona(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            idx = seleccion[0]
            del self.personas[idx]
            self.actualizar_listbox()
            self.limpiar_campos()
        else:
            messagebox.showinfo("Aviso", "Seleccione una persona de la lista para eliminar.")

    def cargar_para_editar(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.indice_edicion = seleccion[0]
            p = self.personas[self.indice_edicion]

            self.limpiar_campos()
            self.txt_nombre.insert(0, p.nombre)
            self.txt_apellidos.insert(0, p.apellidos)
            self.txt_telefono.insert(0, p.telefono)
            self.txt_direccion.insert(0, p.direccion)

            self.btn_guardar.config(state=tk.NORMAL)
            self.btn_anadir.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Aviso", "Seleccione una persona de la lista para editar.")

    def guardar_cambios(self):
        if self.indice_edicion is None:
            return

        nom = self.txt_nombre.get().strip()
        ape = self.txt_apellidos.get().strip()

        if not nom or not ape:
            messagebox.showerror("Error", "Nombre y Apellidos no pueden quedar vacíos.")
            return

        if self.existe_duplicado(nom, ape, indice_ignorado=self.indice_edicion):
            messagebox.showwarning("Registro Duplicado", "¡Alerta! Ya existe otra persona con ese nombre y apellidos.")
            return

        p = self.personas[self.indice_edicion]
        p.nombre = nom
        p.apellidos = ape
        p.telefono = self.txt_telefono.get().strip()
        p.direccion = self.txt_direccion.get().strip()

        self.actualizar_listbox()
        self.limpiar_campos()
        self.btn_guardar.config(state=tk.DISABLED)
        self.btn_anadir.config(state=tk.NORMAL)
        self.indice_edicion = None

    def limpiar_lista(self):
        self.personas.clear()
        self.actualizar_listbox()
        self.limpiar_campos()

    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for p in self.personas:
            self.listbox.insert(tk.END, str(p))

    def limpiar_campos(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_apellidos.delete(0, tk.END)
        self.txt_telefono.delete(0, tk.END)
        self.txt_direccion.delete(0, tk.END)


if __name__ == "__main__":
    app = VentanaPersonas()
    app.mainloop()
