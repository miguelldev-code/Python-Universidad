# Adivinar numero aleatorio del 1 al 10 y en caso de no acertar, 
# decir si es numero ingresado es mas alto o bajo.

# se importa modulo que contiene codigo para ejecutar # aleatorios
import random
                
                #Funcion Random que pide numeros enteros del 1 al 10
numeroAleatorio = random.randint(1,10)

intento = int(input("Adivina un numero del 1 al 10: "))


while intento != numeroAleatorio:
    if intento < numeroAleatorio:
        print("Numero mas alto")
    if intento > numeroAleatorio:
        print("Numero mas bajo")

    intento = int(input("Intenta de nuevo: "))

# SI esta fuera del bucle, quiere decir que se acerto al numeroAleatorio
print("Acertaste!")