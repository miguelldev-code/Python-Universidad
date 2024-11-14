# Diccionario del menú de comida y el de pedidos
menuComida = {
    'Hamburguesa': 5000,
    'Pizza': 3500,
    'Pasta': 3000,
    'Sopa': 1500
}

pedidos = {}  # Llave: nombre del plato, valor: cantidad pedida

# Función para mostrar el menú
def mostrar_menu(menu):
    print("\n-------- Menu ----------")
    print("Plato - Precio")
    for plato, precio in menu.items():
        print(f"{plato} - {precio}")
    print("------------------\n")
    input("Presione enter para continuar")


# Función para realizar un pedido
def realizar_pedido(menu, pedidos):
    while True:
        orden_plato = input("\nPor favor ingrese el plato que deseas pedir: ").strip().capitalize()
        if orden_plato in menu:
            orden_cantidad = input("Por favor ingrese la cantidad del plato que deseas pedir: ")
            if orden_cantidad.isnumeric():
                cantidad = int(orden_cantidad)
                pedidos[orden_plato] = pedidos.get(orden_plato, 0) + cantidad
            else:
                print("La cantidad debe ser un número válido\n")
        else:
            print("El plato no se encuentra en el menú")

        continuar = input("¿Desea seguir pidiendo? (s/n)\n")
        if continuar.lower() == "n":
            break


# Función para ver los pedidos y calcular el total
def ver_pedido(menu, pedidos):
    if not pedidos:
        print("\nNo hay pedidos\n")
        return

    print("\n------------- PEDIDO -----------------------------")
    print("PLATO \t\t-\t CANTIDAD \t-\t PRECIO")
    total = 0
    for plato, cantidad in pedidos.items():
        precio = menu[plato]
        total += precio * cantidad
        print(f"{plato} \t\t-\t {cantidad} \t-\t {precio * cantidad}")
    print(f"\n----- TOTAL:\t\t\t\t\t{total} ------\n")


# Función principal para el bucle de menú
def sistema_pedidos():
    while True:
        print("1. Ver menu")
        print("2. Realizar pedido")
        print("3. Ver pedido")
        print("4. Salir")

        comando = input("\nIngrese el comando: ")

        match comando:
            case "1":
                mostrar_menu(menuComida)
            case "2":
                realizar_pedido(menuComida, pedidos)
            case "3":
                ver_pedido(menuComida, pedidos)
            case "4":
                print("\nEl sistema ha sido finalizado")
                break
            case _:
                print("\nComando no válido\n")


# Ejecutar el sistema de pedidos
sistema_pedidos()
