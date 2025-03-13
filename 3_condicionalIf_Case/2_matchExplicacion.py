

opcion = int(input("Ingrese una opción (1-3): "))

match opcion:
    case 1:
        print("Elegiste la opción 1")
    case 2:
        print("Elegiste la opción 2")
    case 3:
        print("Elegiste la opción 3")
    case _:
        print("Opción no válida")

# match evalúa opcion.
# case compara opcion con valores fijos (1, 2, 3).
# _ funciona como default en switch, ejecutándose si ninguna otra opción coincide.
