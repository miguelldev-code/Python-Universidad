import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area():
    print("\n📏 Seleccione la figura para calcular el área:")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")
    print("4. Cuadrado")

    opcion = input("\nIngrese el número de la figura: ")

    if opcion == "1":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = calcular_area_rectangulo(base, altura)
        print(f"📐 Área del rectángulo: {area:.2f}")

    elif opcion == "2":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = calcular_area_triangulo(base, altura)
        print(f"🔺 Área del triángulo: {area:.2f}")

    elif opcion == "3":
        radio = float(input("Ingrese el radio: "))
        area = calcular_area_circulo(radio)
        print(f"⚪ Área del círculo: {area:.2f}")

    elif opcion == "4":
        lado = float(input("Ingrese el lado: "))
        area = calcular_area_cuadrado(lado)
        print(f"🟪 Área del cuadrado: {area:.2f}")

    else:
        print("❌ Opción no válida. Debe ser un número del 1 al 4.")

calcular_area()
