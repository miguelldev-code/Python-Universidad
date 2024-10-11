import random

numero = int(input("Ingresa un número del 1 al 10: "))

aleatorio = random.randint(1, 10)

print(f"El numero es: {aleatorio}")
if numero == aleatorio:
    print("¡Adivinaste!")
else:
    print("Sigue intentando")
