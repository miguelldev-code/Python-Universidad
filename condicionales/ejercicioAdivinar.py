import random

numeroSecreto = random.randint(1,10)

intento = int(input("Adivina un numero del 1 al 10: "))


while intento != numeroSecreto:
    if intento < numeroSecreto:
        print("Numero mas alto")
    if intento > numeroSecreto:
        print("Numero mas bajo")

    intento = int(input("Intenta de nuevo: "))


print("Acertaste!")