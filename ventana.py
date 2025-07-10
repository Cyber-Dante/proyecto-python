from tkinter import *

root = Tk()
root.title("Formulario de roles")
root.geometry("350x400")

# ---------- Variables ----------
sexo = StringVar(value="Mujer")  # Por defecto
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

    if sexo.get() == "Mujer":
        checkboxes["Siervo ministerial"].config(state="disabled")
        checkboxes["Anciano"].config(state="disabled")
        roles["Siervo ministerial"].set(0)
        roles["Anciano"].set(0)
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
    else:
        # Rehabilitar checkboxes según condiciones
        checkboxes["Publicador bautizado"].config(state="normal")
        checkboxes["Precursor auxiliar"].config(state="normal")
        checkboxes["Precursor regular"].config(state="normal")

        if sexo.get() == "Hombre":
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
        if sexo.get() == "Hombre" and roles["Publicador no bautizado"].get() == 0:
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

Label(root, text="Seleccione sexo:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10, 0))

frame_radio = Frame(root)
frame_radio.pack(anchor="w", padx=20)

Radiobutton(frame_radio, text="Hombre", variable=sexo, value="Hombre", command=actualizar_roles).pack(anchor="w")
Radiobutton(frame_radio, text="Mujer", variable=sexo, value="Mujer", command=actualizar_roles).pack(anchor="w")

Label(root, text="Seleccione roles:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10, 0))

frame_check = Frame(root)
frame_check.pack(anchor="w", padx=20)

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

root.mainloop()
