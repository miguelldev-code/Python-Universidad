menuComida = {
    'Hamburguesa': 5000,
    'Pizza': 3500,
    'Pasta': 3000,
    'Sopa': 1500
}

# Diccionario para almacenar los pedidos
pedidos = {}  # Llave: nombre del plato, valor: cantidad pedida
total = 0     # Variable para almacenar el total a pagar por los pedidos

# Bucle principal del sistema
while True:
    # Mostrar las opciones del menú principal
    print("1. Ver menu")         # Opción para ver el menú
    print("2. Realizar pedido")  # Opción para hacer un pedido
    print("3. Ver pedido")       # Opción para revisar el pedido actual
    print("4. Salir")            # Opción para salir del sistema
    comando = input("\nIngrese el comando: ")  # Recibe el comando del usuario

    # Manejo del comando usando match-case
    match comando:
        case "1":  # Mostrar el menú al usuario
            print("\n--------Menu----------")
            print("Plato - Precio")  # Encabezado del menú
            # Ciclo para mostrar todos los platos con sus precios
            for plato, precio in menuComida.items():
                print(f"{plato} - {precio}")
            print("------------------\n")
            input("Presione enter para continuar")  # Pausa para que el usuario pueda leer el menú

        case "2":  # Permitir al usuario hacer un pedido
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

        case "3":  # Mostrar los pedidos realizados y calcular el total
            if not pedidos:
                print("\nNo hay pedidos\n")  # Mostrar mensaje si no hay pedidos realizados
                continue

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

        case "4":  # Salir del sistema
            print("\nEl sistema ha sido finalizado")
            break  # Romper el bucle para salir

        case _:  # Caso por defecto para comandos no válidos
            print("\nComando no válido\n")  # Mostrar mensaje de error si el comando no es reconocido
