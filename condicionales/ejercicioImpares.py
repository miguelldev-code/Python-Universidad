# Ingresar numero positivo e imprimir impares

#    Practica WHILE para validacion
numero = int(input("Ingresa un numero entero positivo: "))
while numero < 0:   
    print("No es positivo")
    numero = int(input("Ingresa un numero entero positivo: "))
    continue

print(f"El numero es: {numero}")

#       Practica FOR
#             inicio,final,incremento 
for i in range(1, numero+1, 2):
    print(i, end=",")