# Programa que contiene un menú con platos y precios.
# Ofrece opciones para ver el menú, realizar pedidos, ver los pedidos actuales o salir.
# Al pedir, el usuario ingresa el plato y cantidad, y el sistema valida si está disponible.
# Los pedidos se almacenan y luego pueden visualizarse con su costo total.
# Si se selecciona salir, el programa termina.
# Maneja entradas inválidas mostrando un mensaje de error.

# Definir el menú de comidas: una lista que contiene los nombres de los platos disponibles.

# Definir los precios correspondientes a cada plato en el menú.

# Crear listas vacías para almacenar los platos pedidos y la cantidad de cada pedido.

# Crear una variable para almacenar el total del costo de los pedidos.

# Iniciar un bucle que funcione como el menú principal del sistema de pedidos.

    # Mostrar al usuario las opciones:
    # 1. Ver menú
    # 2. Realizar pedido
    # 3. Ver pedido
    # 4. Salir del sistema

    # Solicitar al usuario que ingrese un comando (una opción del menú).

    # Usar una estructura de control (como un switch o match-case) para manejar cada comando ingresado:

        # Opción 1: Mostrar el menú.
            # Imprimir una lista de los platos disponibles junto con sus precios.
            # Pausar el programa para que el usuario pueda leer el menú antes de continuar.

        # Opción 2: Realizar un pedido.
            # Iniciar un bucle para permitir al usuario hacer varios pedidos.
                # Solicitar al usuario que ingrese el nombre del plato que desea pedir.
                # Verificar si el plato ingresado está disponible en el menú.
                # Si está disponible:
                    # Solicitar al usuario que ingrese la cantidad de ese plato.
                    # Verificar que la cantidad ingresada sea un número válido.
                    # Si es válida, agregar el plato y la cantidad a las listas de pedidos.
                # Si no está disponible, mostrar un mensaje indicando que el plato no existe en el menú.
                # Preguntar al usuario si desea continuar haciendo más pedidos.
                # Si el usuario decide no continuar, salir del bucle de pedidos.

        # Opción 3: Ver el pedido actual.
            # Verificar si hay pedidos realizados.
                # Si no hay pedidos, mostrar un mensaje indicando que no hay pedidos.
                # Si hay pedidos:
                    # Mostrar una tabla con los platos pedidos, las cantidades y el costo de cada uno.
                    # Calcular el total del pedido sumando el precio de cada plato multiplicado por la cantidad.
                    # Mostrar el total a pagar.

        # Opción 4: Salir del sistema.
            # Finalizar el bucle principal y mostrar un mensaje indicando que el sistema ha sido cerrado.

        # Opción por defecto: Manejar entradas inválidas.
            # Mostrar un mensaje indicando que el comando ingresado no es válido.






# Definición del menú y precios
menuComida = [
    'Hamburguesa',  # Opción de Hamburguesa en el menú
    'Pizza',        # Opción de Pizza en el menú
    'Pasta',        # Opción de Pasta en el menú
    'Sopa'          # Opción de Sopa en el menú
]

precios = [5000, 3500, 3000, 1500]  # Precios correspondientes a cada plato en el menú

# Listas para almacenar los pedidos
pedidosComida = []   # Aquí se guardan los platos que el usuario pide
pedidosCantidad = [] # Aquí se guardan las cantidades de cada plato que el usuario pide
total = 0            # Variable para almacenar el total a pagar por los pedidos

# Bucle principal del sistema
while True:
    # Mostrar las opciones del menú principal
    print("1. Ver menu")      # Opción para ver el menú
    print("2. Realizar pedido")  # Opción para hacer un pedido
    print("3. Ver pedido")     # Opción para revisar el pedido actual
    print("4. Salir")          # Opción para salir del sistema
    comando = input("\nIngrese el comando: ")  # Recibe el comando del usuario

    # Manejo del comando usando match-case
    match comando:
        case "1":  # Mostrar el menú al usuario
            print("\n--------Menu----------")
            print("Plato - Precio")  # Encabezado del menú
            # Ciclo para mostrar todos los platos con sus precios
            for i in range(len(menuComida)):
                print(f"{menuComida[i]} - {precios[i]}")
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
                        # Agregar el plato y la cantidad a las listas de pedidos
                        pedidosComida.append(ordenPlato)
                        pedidosCantidad.append(int(ordenPlatoCantidad))
                    else:
                        print("\nLa cantidad debe ser un número\n")
                else:
                    print("\nEl plato no se encuentra en el menú")  # Mensaje si el plato no está disponible
                # Preguntar si el usuario desea seguir haciendo pedidos
                continuar = input("¿Desea seguir pidiendo? (s/n)\n")
                if continuar.lower() == "n":
                    break  # Salir del bucle si el usuario no quiere seguir pidiendo

        case "3":  # Mostrar los pedidos realizados y calcular el total
            if len(pedidosComida) == 0 and len(pedidosCantidad) == 0:
                print("\nNo hay pedidos\n")  # Mostrar mensaje si no hay pedidos realizados
                continue

            print("\n-------------PEDIDO-----------------------------")
            print(f"PLATO \t\t-\t CANTIDAD \t-\t PRECIO\n")
            total = 0  # Reiniciar el total antes de calcular los pedidos
            # Ciclo para mostrar cada pedido con su cantidad y precio
            for index in range(len(pedidosComida)):
                existencia = menuComida.index(pedidosComida[index])  # Obtener el índice del plato en el menú
                # Calcular el total sumando los precios por la cantidad de cada plato
                total += precios[existencia] * pedidosCantidad[index]
                print(f"{pedidosComida[index]} \t\t-\t {pedidosCantidad[index]} \t-\t {total}")

            # Mostrar el total final a pagar
            print(f"\n-----TOTAL:\t\t\t\t\t{total}------\n")

        case "4":  # Salir del sistema
            print("\nEl sistema ha sido finalizado")
            break  # Romper el bucle para salir

        case _:  # Caso por defecto para comandos no válidos
            print("\nComando no válido\n")  # Mostrar mensaje de error si el comando no es reconocido
