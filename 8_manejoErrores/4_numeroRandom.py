import random

def jugar():
    secreto = random.randint(1, 10)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (1-10): "))
            intentos += 1

            if intento == secreto:
                print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos.")
                break
            elif intento < secreto:
                print("Muy bajo ⬇️")
            else:
                print("Muy alto ⬆️")
        except ValueError:
            print("❌ Ingresa un número válido.")

jugar()
