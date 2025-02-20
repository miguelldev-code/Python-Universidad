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
    print("1️⃣ Rectángulo")
    print("2️⃣ Triángulo")
    print("3️⃣ Círculo")
    print("4️⃣ Cuadrado")

    opcion = input("\nIngrese el número de la figura: ")

    match opcion:
        case "1":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = calcular_area_rectangulo(base, altura)
            print(f"📐 Área del rectángulo: {area}")

        case "2":
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            area = calcular_area_triangulo(base, altura)
            print(f"🔺 Área del triángulo: {area}")

        case "3":
            radio = float(input("Ingrese el radio: "))
            area = calcular_area_circulo(radio)
            print(f"⚪ Área del círculo: {area}")

        case "4":
            lado = float(input("Ingrese el lado: "))
            area = calcular_area_cuadrado(lado)
            print(f"🟪 Área del cuadrado: {area:.2f}")

        case _:
            print("❌ Opción no válida. Debe ser un número del 1 al 4.")

calcular_area()
