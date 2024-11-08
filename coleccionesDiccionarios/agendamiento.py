#                       AGENDA DE CONTACTOS                   

# Funciones básicas para agregar, buscar, actualizar, eliminar y ver contactos.

# Diccionario para almacenar la agenda de contactos
# Cada contacto se guarda en el diccionario como un par clave-valor, donde:
# - La clave es el nombre del contacto.
# - El valor es el número de teléfono.
agenda = {}

while True:
    # Menú de acciones para gestionar contactos

    print("\nOpciones disponibles:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos los contactos")
    print("6. Salir")

    accion = input("\nSelecciona una opción (1-6): ")

    match accion:
        case "1":  # Agregar contacto
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado.")

        case "2":  # Buscar contacto
            nombre = input("Nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Teléfono de {nombre}: {agenda[nombre]}")
            else:
                print("Contacto no encontrado.")

        case "3":  # Actualizar contacto
            nombre = input("Nombre del contacto a actualizar: ")
            if nombre in agenda:
                telefono = input("Nuevo número de teléfono: ")
                agenda[nombre] = telefono
                print(f"Contacto '{nombre}' actualizado.")
            else:
                print("Contacto no encontrado.")

        case "4":  # Eliminar contacto
            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto '{nombre}' eliminado.")
            else:
                print("Contacto no encontrado.")

        case "5":  # Ver todos los contactos
            if agenda:
                print("\nAgenda de contactos:")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("La agenda está vacía.")

        case "6":  # Salir del programa
            print("Saliendo de la agenda de contactos.")
            break

        case _:  # Opción no válida
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")
