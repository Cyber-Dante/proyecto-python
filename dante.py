persona_1 = {
    "nombre": "Dante",
    "apellido": "Aguero",
    "edad": 14,
    "genero": "Masculino"
}

persona_2 = {
    "nombre" : "Gimena",
    "apellido" : "Perez"
 }

persona_3 = {
    "nombre" : "Nicolas",
    "apellido" : "Cano"
}


def renombrarJuan():
    for persona in [persona_1, persona_2, persona_3]:
        persona ["nombre"] = "Juan"
        print(persona["nombre"])

renombrarJuan()