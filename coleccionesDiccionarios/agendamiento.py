agenda = {}

while True:
    accion = input("¿Qué quieres hacer? (agregar, buscar, actualizar, eliminar, ver, salir): ")

    if accion == "agregar":
        nombre = input("Nombre del contacto: ")
        telefono = input("Número de teléfono: ")
        agenda[nombre] = telefono
        print("Contacto agregado.")

    elif accion == "buscar":
        nombre = input("Nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Teléfono de {nombre}: {agenda[nombre]}")
        else:
            print("Contacto no encontrado.")

    elif accion == "actualizar":
        nombre = input("Nombre del contacto a actualizar: ")
        if nombre in agenda:
            telefono = input("Nuevo número de teléfono: ")
            agenda[nombre] = telefono
            print("Contacto actualizado.")
        else:
            print("Contacto no encontrado.")

    elif accion == "eliminar":
        nombre = input("Nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")

    elif accion == "ver":
        print("Agenda de contactos:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")

    elif accion == "salir":
        break
    else:
        print("Acción no válida.")
