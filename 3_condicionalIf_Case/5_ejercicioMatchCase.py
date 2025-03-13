"""Crea un programa que muestre un menú con las siguientes opciones:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir

El usuario debe ingresar dos números y elegir una opción. 
El programa usará match-case para realizar la operación correspondiente."""


print("📌 MENÚ DE OPERACIONES 📌")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Elige una opción (1-4): "))

num1 = float(input("Ingresa el primer número: "))    
num2 = float(input("Ingresa el segundo número: "))

match opcion:
    case 1:
        resultado = num1 + num2
        print(f"La suma es: {resultado}")
    case 2:
        resultado = num1 - num2
        print(f"La resta es: {resultado}")
    case 3:
        resultado = num1 * num2
        print(f"La multiplicación es: {resultado}")
    case 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división es: {resultado}")
        else:
            print("Error: No se puede dividir por cero.")
    case _:
        print("Opción no válida. Intenta de nuevo.")
