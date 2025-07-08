import random

# Lista de palabras posibles
palabras = ['python', 'computadora', 'programa', 'juego', 'teclado']
palabra_secreta = random.choice(palabras)

# Variables del juego
letras_adivinadas = []
intentos = 6

print("🎯 ¡Bienvenido al juego del Ahorcado!")
print("_ " * len(palabra_secreta))

# Bucle principal del juego
while intentos > 0:
    letra = input("🔠 Adivina una letra: ").lower()

    if letra in letras_adivinadas:
        print("⛔ Ya adivinaste esa letra. Intenta otra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra_secreta:
        print("✅ ¡Bien! La letra está en la palabra.")
    else:
        intentos -= 1
        print(f"❌ Letra incorrecta. Te quedan {intentos} intentos.")

    # Mostrar progreso
    palabra_mostrada = ''
    for letra_secreta in palabra_secreta:
        if letra_secreta in letras_adivinadas:
            palabra_mostrada += letra_secreta + ' '
        else:
            palabra_mostrada += '_ '

    print("🟦 " + palabra_mostrada)

    # Verificar si ganó
    if all(letra in letras_adivinadas for letra in palabra_secreta):
        print("🎉 ¡Ganaste! La palabra era:", palabra_secreta)
        break

# Si se queda sin intentos
if intentos == 0:
    print("💀 ¡Perdiste! La palabra era:", palabra_secreta)