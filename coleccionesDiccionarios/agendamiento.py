

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

    if accion == "1":  # Agregar contacto
        # Solicita el nombre y número de teléfono del nuevo contacto
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        
        # Almacena el contacto en `agenda` usando el nombre como clave y el teléfono como valor
        # Si el contacto ya existe, se sobrescribe el número de teléfono
        agenda[nombre] = telefono
        print(f"Contacto '{nombre}' agregado.")

    elif accion == "2":  # Buscar contacto
        # Solicita el nombre del contacto a buscar
        nombre = input("Nombre del contacto a buscar: ")
        
        # Verifica si el nombre existe como clave en `agenda`
        if nombre in agenda:
            # Si el contacto existe, accede al número de teléfono (valor asociado a la clave `nombre`)
            print(f"Teléfono de {nombre}: {agenda[nombre]}")
        else:
            # Si el contacto no está en `agenda`, muestra un mensaje
            print("Contacto no encontrado.")

    elif accion == "3":  # Actualizar contacto
        # Solicita el nombre del contacto a actualizar
        nombre = input("Nombre del contacto a actualizar: ")
        
        # Verifica si el contacto existe en `agenda`
        if nombre in agenda:
            # Si existe, solicita el nuevo número y lo actualiza
            telefono = input("Nuevo número de teléfono: ")
            agenda[nombre] = telefono  # Actualiza el valor de la clave `nombre`
            print(f"Contacto '{nombre}' actualizado.")
        else:
            # Si el contacto no está en `agenda`, muestra un mensaje
            print("Contacto no encontrado.")

    elif accion == "4":  # Eliminar contacto
        # Solicita el nombre del contacto a eliminar
        nombre = input("Nombre del contacto a eliminar: ")
        
        # Verifica si el contacto existe en `agenda`
        if nombre in agenda:
            # Si existe, elimina la entrada (par clave-valor) usando `del`
            del agenda[nombre]
            print(f"Contacto '{nombre}' eliminado.")
        else:
            # Si el contacto no está en `agenda`, muestra un mensaje
            print("Contacto no encontrado.")

    elif accion == "5":  # Ver todos los contactos
        # Verifica si `agenda` tiene contactos
        if agenda:
            print("\nAgenda de contactos:")
            # Usa un bucle para recorrer y mostrar cada par clave-valor en `agenda`
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            # Si `agenda` está vacía, informa que no hay contactos
            print("La agenda está vacía.")

    elif accion == "6":  # Salir del programa
        print("Saliendo de la agenda de contactos.")
        break
    else:
        # Informa al usuario si la opción ingresada no es válida
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")
