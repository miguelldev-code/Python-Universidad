# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y escriba el mayor, el menor y la media aritmética.

# Se recuerda que la media aritmética de un conjunto de valores es la suma
# de esos valores dividida por la cantidad de valores.

# VALIDACION OCN WHILE
cantidadNumeros = int(input("Ingresa la cantidad de numeros: "))
while cantidadNumeros <= 0:
    print(f"El numero debe ser mayor a 0")
    cantidadNumeros = int(input("Ingresa la cantidad de numeros: "))

# CREACION DE VARIABLES
numero = int(input("Ingresa el numero 1: "))
maximo = numero
minimo = numero
suma = numero

# RECORRIDO DE NUMEROS, HALLAR MAX Y MIN Y SUMATORIA
for i  in range(2, cantidadNumeros + 1):
    numero = float(input(f"Ingresa el numero {i}: "))
    if numero > maximo:
        maximo = numero

    if numero < minimo:
        minimo = numero

    suma += numero

# HALLAR MEDIA
media = suma/cantidadNumeros

# IMPRESION DE RESULTADOS
print(f"El numero maximo es {maximo}")
print(f"El numero minimo es {minimo}")
print(f"La media de los numeros es {media}")



