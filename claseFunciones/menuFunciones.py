menuComida = {
    'Hamburguesa': 5000,
    'Pizza': 3500,
    'Pasta': 3000,
    'Sopa': 1500
}

# Diccionario para almacenar los pedidos
pedidos = {}  # Llave: nombre del plato, valor: cantidad pedida

def mostrar_menu(menu):
    print("\n--------Menu----------")
    print("Plato - Precio")  # Encabezado del menú
    # Ciclo para mostrar todos los platos con sus precios
    for plato, precio in menuComida.items():
        print(f"{plato} - {precio}")
    print("------------------\n")
    input("Presione enter para continuar") 

def realizar_pedido(menu, pedidos):
    while True:
        # Pedir el nombre del plato al usuario
        ordenPlato = input("\nPor favor ingrese el plato que deseas pedir: ").strip().capitalize()
        # Verificar si el plato está en el menú
        if ordenPlato in menuComida:
            # Pedir la cantidad de platos que desea el usuario
            ordenPlatoCantidad = input("\nPor favor ingrese la cantidad del plato que deseas pedir: ")
            # Verificar si la cantidad es un número válido
            if ordenPlatoCantidad.isnumeric():
                # Agregar el plato y la cantidad al diccionario de pedidos
                if ordenPlato in pedidos:
                    pedidos[ordenPlato] += int(ordenPlatoCantidad)  # Sumar cantidad si ya existe en el pedido
                else:
                    pedidos[ordenPlato] = int(ordenPlatoCantidad)   # Agregar nuevo plato
            else:
                print("\nLa cantidad debe ser un número\n")
        else:
            print("\nEl plato no se encuentra en el menú")  # Mensaje si el plato no está disponible
        # Preguntar si el usuario desea seguir haciendo pedidos
        continuar = input("¿Desea seguir pidiendo? (s/n)\n")
        if continuar.lower() == "n":
            break  # Salir del bucle si el usuario no quiere seguir pidiendo

def ver_pedido(menu, pedidos):
    if not pedidos:
        print("\nNo hay pedidos\n")  # Mostrar mensaje si no hay pedidos realizados
        return

    print("\n-------------PEDIDO-----------------------------")
    print(f"PLATO \t\t-\t CANTIDAD \t-\t PRECIO\n")
    total = 0  # Reiniciar el total antes de calcular los pedidos
    # Ciclo para mostrar cada pedido con su cantidad y precio
    for plato, cantidad in pedidos.items():
        # SE LLAMA EL PRECIO DE CADA PLATO
        precio = menuComida[plato]
        total += precio * cantidad
        print(f"{plato} \t\t-\t {cantidad} \t-\t {precio * cantidad}")

    # Mostrar el total final a pagar
    print(f"\n-----TOTAL:\t\t\t\t\t{total}------\n")


def sistema_pedidos():
        while True:
            # Mostrar las opciones del menú principal
            print("1. Ver menu")         # Opción para ver el menú
            print("2. Realizar pedido")  # Opción para hacer un pedido
            print("3. Ver pedido")       # Opción para revisar el pedido actual
            print("4. Salir")            # Opción para salir del sistema
            comando = input("\nIngrese el comando: ")

            match comando:
                case "1":
                    mostrar_menu(menuComida)
                case "2":
                    realizar_pedido(menuComida, pedidos)
                case "3":
                    ver_pedido(menuComida, pedidos)
                case"4":
                    print("El sistema ha finalizado")
                    break
                case _:
                    print("Comando no valido")


sistema_pedidos()