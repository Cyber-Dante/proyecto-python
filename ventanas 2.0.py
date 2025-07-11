from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ejemplo con lista desplegable")
root.geometry("300x150")

# Opciones de la lista
opciones = ["Congregación A", "Congregación B", "Congregación C"]

# Variable para almacenar la selección
congregacion = StringVar()

# Crear Combobox
combo = ttk.Combobox(root, textvariable=congregacion, state="readonly")
combo['values'] = opciones
combo.set("Elija una congregación")  # Placeholder simulado
combo.pack(pady=20)

# Función para verificar la selección
def verificar():
    seleccion = congregacion.get()
    if seleccion == "Elija una congregación":
        print("Por favor, elija una opción válida.")
    else:
        print("Seleccionaste:", seleccion)

Button(root, text="Aceptar", command=verificar).pack()

root.mainloop()
