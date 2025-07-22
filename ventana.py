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
fecha_bautismo = DateEntry(frame_A, selectmode='BROWSE', date_pattern='dd/mm/yyyy', locale="es_AR", width=20, textvariable=datos_publicador["fecha_bautismo"])
fecha_bautismo.grid(row=2, column=1)

# ---------- congregacion ----------
# Opciones de la lista
opciones = ["Congregación Media Agua", "Congregación Santa Rosa ", "Congregación Pocitos", "Congregacion centro"]

# Variable para almacenar la selección
congregacion = StringVar()

# Crear Combobox col2 row1
combo = ttk.Combobox(root, textvariable=congregacion, state="readonly")
combo['values'] = opciones
combo.set("Elija una congregación")  # Placeholder simulado
combo.grid(row=0, column=1, pady=3)

# Función para verificar la selección
def verificar():
    seleccion = congregacion.get()
    if seleccion == "Elija una congregación":
        print("Por favor, elija una opción válida.")
    else:
        datos_publicador["congregacion"] = seleccion

# ---------- Inputs para nombre y apellido ----------
Label(frame_A, text="Nombre:", font=("Arial", 12)).grid(row=0, column=0, pady=3)
Entry(frame_A, textvariable=datos_publicador["nombre"]).grid(row=0, column=1, pady=3)
Label(frame_A, text="Apellido:", font=("Arial", 12)).grid(row=1, column=0, pady=3)
Entry(frame_A, textvariable=datos_publicador["apellido"]).grid(row=1, column=1, pady=3)

def fecha_bautismo():
    datos_publicador["fecha_bautismo"] = fecha_bautismo.get_date()

# ---------- Variables ----------
genero = StringVar(value="Mujer")  # Por defecto
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
    """Actualizar roles según el género y el estado actual."""
    if roles["Publicador no bautizado"].get() == 1:
        validar_publicador_conflictos()
        return

    if genero.get() == "Hombre":
        checkboxes["Siervo ministerial"].config(state="disabled")
        checkboxes["Anciano"].config(state="disabled")
        roles["Siervo ministerial"].set(0)
        roles["Anciano"].set(0)
        datos_publicador["genero"] = "Hombre"
    else:
        checkboxes["Siervo ministerial"].config(state="normal")
        checkboxes["Anciano"].config(state="normal")

    validar_publicador_conflictos()
    validar_rol_exclusivo()
    validar_si_precursor_auxiliar()

def validar_publicador_conflictos():
    """Si se marca Publicador, desactivar todas las otras opciones de roles."""
    if roles["Publicador no bautizado"].get() == 1:
        # Desactivar todos los checkboxes excepto Publicador
        for key in roles:
            if key != "Publicador no bautizado":
                checkboxes[key].config(state="disabled")
                roles[key].set(0)
                datos_publicador[key] = 0
    else:
        # Rehabilitar checkboxes según condiciones
        checkboxes["Publicador bautizado"].config(state="normal")
        checkboxes["Precursor auxiliar"].config(state="normal")
        checkboxes["Precursor regular"].config(state="normal")

        if genero.get() == "Hombre":
            checkboxes["Siervo ministerial"].config(state="normal")
            checkboxes["Anciano"].config(state="normal")
        else:
            checkboxes["Siervo ministerial"].config(state="disabled")
            checkboxes["Anciano"].config(state="disabled")

        validar_rol_exclusivo()
        validar_si_precursor_auxiliar()

def validar_rol_exclusivo():
    """Evita marcar Siervo y Anciano a la vez."""
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
    """Evita marcar ambos: Precursor auxiliar y regular al mismo tiempo."""
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

Label(root, text="Seleccione género:", font=("Arial", 12)).grid(row=1, column=0, pady=3)
frame_radio = Frame(root)
frame_radio.grid(row=1, column=1, pady=3)

genero = StringVar(value="Mujer")

datos_publicador["genero"] = genero

Radiobutton(frame_radio, text="Hombre", variable=genero, value="Hombre", command=actualizar_roles).pack(anchor="w")
Radiobutton(frame_radio, text="Mujer", variable=genero, value="Mujer", command=actualizar_roles).pack(anchor="w")


# ---------- Roles ----------
Label(root, text="Seleccione roles:", font=("Arial", 12)).grid(row=2, column=0, pady=3)

frame_check = Frame(root)
frame_check.grid(row=2, column=1, pady=3)

for texto, var in roles.items():
    if texto == "Publicador no bautizado":
        chk = Checkbutton(frame_check, text=texto, variable=var, command=actualizar_roles)
    elif texto in ["Siervo ministerial", "Anciano"]:
        chk = Checkbutton(frame_check, text=texto, variable=var, command=validar_rol_exclusivo)
    elif texto in ["Precursor auxiliar", "Precursor regular"]:
        chk = Checkbutton(frame_check, text=texto, variable=var, command=validar_si_precursor_auxiliar)
    else:
        chk = Checkbutton(frame_check, text=texto, variable=var)
    chk.pack(anchor="w")
    checkboxes[texto] = chk

# Inicializar
actualizar_roles()

# ---------- Funciones ----------
def guardar_publicador():
    print("Guardando publicador...")
    for propiedad in datos_publicador:
        print(propiedad, datos_publicador[propiedad].get())

Button(root, text="Guardar", command=guardar_publicador).grid(row=3, column=1, pady=3)

root.mainloop()








