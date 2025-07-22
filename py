from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()
root.title("Formulario de roles")
root.geometry("700x700")

# ---------- variable global ----------
datos_publicador = {
    "nombre": StringVar(),
    "apellido": StringVar(),
    "fecha_bautismo": StringVar(),
    "genero": StringVar(),
    "privilegio": StringVar(),
    "congregacion": StringVar()
}

# Grid 2 rows 2 cols
frame_A = Frame(root, borderwidth=1, relief="solid")
frame_B = Frame(root, borderwidth=1, relief="solid")
frame_C = Frame(root, borderwidth=1, relief="solid")
frame_D = Frame(root, borderwidth=1, relief="solid")

frame_A.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame_B.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
frame_C.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
frame_D.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

Label(frame_A, text="Nombre:").grid(row=0, column=0)
Entry(frame_A, textvariable=datos_publicador["nombre"]).grid(row=0, column=1)

Label(frame_A, text="Apellido:").grid(row=1, column=0)
Entry(frame_A, textvariable=datos_publicador["apellido"]).grid(row=1, column=1)

Label(frame_A, text="Fecha de bautismo:").grid(row=2, column=0)
fecha_bautismo = DateEntry(frame_A, selectmode='BROWSE', date_pattern='dd/mm/yyyy', locale="es_AR", width=20)
fecha_bautismo.grid(row=2, column=1)

# ---------- congregacion ----------
opciones = ["Congregación Media Agua", "Congregación Santa Rosa ", "Congregación Pocitos", "Congregacion centro"]
congregacion = StringVar()
combo = ttk.Combobox(frame_C, textvariable=congregacion, state="readonly")
combo['values'] = opciones
combo.set("Elija una congregación")
combo.pack(pady=10)

# ---------- Variables ----------
genero = StringVar(value="Mujer")  # Por defecto
datos_publicador["genero"] = genero

roles = {
    "Publicador no bautizado": IntVar(),
    "Publicador bautizado": IntVar(),
    "Precursor auxiliar": IntVar(),
    "Precursor regular": IntVar(),
    "Siervo ministerial": IntVar(),
    "Anciano": IntVar()
}
checkboxes = {}

# ---------- Funciones ----------

def actualizar_roles():
    if roles["Publicador no bautizado"].get() == 1:
        for key in roles:
            if key != "Publicador no bautizado":
                checkboxes[key].config(state="disabled")
                roles[key].set(0)
        return

    for key in roles:
        checkboxes[key].config(state="normal")

    if genero.get() == "Mujer":
        checkboxes["Siervo ministerial"].config(state="disabled")
        checkboxes["Anciano"].config(state="disabled")
        roles["Siervo ministerial"].set(0)
        roles["Anciano"].set(0)

    validar_rol_exclusivo()
    validar_si_precursor_auxiliar()

def validar_rol_exclusivo():
    if roles["Siervo ministerial"].get() == 1:
        checkboxes["Anciano"].config(state="disabled")
        roles["Anciano"].set(0)
    elif roles["Anciano"].get() == 1:
        checkboxes["Siervo ministerial"].config(state="disabled")
        roles["Siervo ministerial"].set(0)
    else:
        if genero.get() == "Hombre" and roles["Publicador no bautizado"].get() == 0:
            checkboxes["Siervo ministerial"].config(state="normal")
            checkboxes["Anciano"].config(state="normal")

def validar_si_precursor_auxiliar():
    if roles["Precursor auxiliar"].get() == 1:
        checkboxes["Precursor regular"].config(state="disabled")
        roles["Precursor regular"].set(0)
    elif roles["Precursor regular"].get() == 1:
        checkboxes["Precursor auxiliar"].config(state="disabled")
        roles["Precursor auxiliar"].set(0)
    else:
        checkboxes["Precursor auxiliar"].config(state="normal")
        checkboxes["Precursor regular"].config(state="normal")

# ---------- Interfaz ----------
Label(frame_B, text="Seleccione género:", font=("Arial", 12)).pack(pady=5)

frame_radio = Frame(frame_B)
frame_radio.pack()

Radiobutton(frame_radio, text="Hombre", variable=genero, value="Hombre", command=actualizar_roles).pack(anchor="w")
Radiobutton(frame_radio, text="Mujer", variable=genero, value="Mujer", command=actualizar_roles).pack(anchor="w")

# ---------- Roles ----------
Label(frame_D, text="Seleccione roles:", font=("Arial", 12)).pack(pady=5)

frame_check = Frame(frame_D)
frame_check.pack()

for texto, var in roles.items():
    chk = Checkbutton(frame_check, text=texto, variable=var, command=actualizar_roles)
    chk.pack(anchor="w")
    checkboxes[texto] = chk

# ---------- Botón Guardar ----------
def guardar_publicador():
    datos_publicador["fecha_bautismo"].set(fecha_bautismo.get_date())
    datos_publicador["congregacion"].set(congregacion.get())
    print("\n--- DATOS GUARDADOS ---")
    for campo, var in datos_publicador.items():
        print(f"{campo}: {var.get()}")
    for rol, var in roles.items():
        if var.get():
            print(f"Rol activo: {rol}")

Button(root, text="Guardar", command=guardar_publicador).grid(row=2, column=0, columnspan=2, pady=10)

# Inicializar
actualizar_roles()

root.mainloop()
