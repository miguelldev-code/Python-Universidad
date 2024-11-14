import math 

# Area de rectangulo, truangulo, circulo y cuadrado

def calculoRectangulo(base, altura):
    return base * altura

def calculoTriangulo(base, altura):
    return (base * altura)/2

def calculoCirculo(radio):
    return math.pi * radio ** 2

def calculoCuadrado(lado):
    return lado * lado

def calculoFIgura():
    print("Seleccione la figura para calcular el area")
    print("1. Rectangulo")
    print("2. Triangulo")
    print("3. Circulo")
    print("4. Cuadrado")

    opcion = input("Ingrese el numero de la figura")

    match opcion:
        case "1":
            base = float(input("Ingrese la base"))
            altura = float(input("Ingrese la altura"))
            area = calculoRectangulo(base, altura)
            print("Area del rectangulo", area)
        case "2":
            base = float(input("Ingrese la base"))
            altura = float(input("Ingrese la altura"))
            area = calculoTriangulo(base, altura)
            print("Area del rectangulo", area)
        
        case "3":
            radio = float(input("Ingrese la base"))
            area = calculoCirculo(radio)
            print("Area del rectangulo", area)
        
        case "4":
            lado = float(input("Ingrese la base"))
            area = calculoCuadrado(lado)
            print("Area del rectangulo", area)

        case _:
            print("Opcion no valida, elija del 1 al 4")



calculoFIgura()