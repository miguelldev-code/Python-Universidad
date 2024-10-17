# Escriba un programa que pregunte cuántos números se van 
# a introducir, pida esos números, y muestre un mensaje 
# cada vez que un número no sea mayor que el PRIMERO.

cantidadNumeros = int(input("Ingrese la cantidad de numeros a pedir: "))

while cantidadNumeros <= 0:
    print(f"El numero {cantidadNumeros}, no es valido")
    cantidadNumeros = int(input("Ingrese la cantidad de numeros a pedir: "))

numero = int(input("Ingresa un numero: "))

#            incio,    final
for i in range(1, cantidadNumeros):
    numeroMayor = int(input(f"Ingresa un numero mayor a {numero}: "))
    if numeroMayor <= numero:
        print(f"{numeroMayor} no es mayor que {numero}")
    # 
    # numero = numeroMayor

print("Fin del programa")


