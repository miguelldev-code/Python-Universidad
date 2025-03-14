import math
    
# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    return lado ** 2

# Función principal para seleccionar y calcular el área de la figura deseada
def calcular_area_figura():
    print("Seleccione la figura para calcular el área:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Cuadrado")

    opcion = input("Ingrese el número de la figura: ")

    # Selección de la figura geométrica usando match-case
    match opcion:
        case "1":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = calcular_area_rectangulo(base, altura)
            print("Área del rectángulo:", area)

        case "2":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = calcular_area_triangulo(base, altura)
            print("Área del triángulo:", area)

        case "3":
            radio = float(input("Ingrese el radio del círculo: "))
            area = calcular_area_circulo(radio)
            print("Área del círculo:", area)

        case "4":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print("Área del cuadrado:", area)

        case _:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")

# Llamada a la función principal
calcular_area_figura()
