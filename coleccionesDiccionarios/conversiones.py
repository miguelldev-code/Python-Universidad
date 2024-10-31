conversiones = {
    ("metros", "kilometros"): 0.001,
    ("kilometros", "metros"): 1000,
    ("millas", "kilometros"): 1.60934,
    ("kilometros", "millas"): 0.621371,
    # Añadir más conversiones aquí
}

while True:

    for opciones in conversiones.keys():
        print(f"{opciones[0]} a {opciones[1]}")

    accion = input("¿Quieres convertir? (s, n): ").strip().lower()

    match accion:
        case "s":
            cantidad = float(input("Cantidad: "))

            unidad_origen = input("Unidad origen: ").strip().lower()
            unidad_destino = input("Unidad destino: ").strip().lower()

            if (unidad_origen, unidad_destino) in conversiones:
                factor = conversiones[(unidad_origen, unidad_destino)]
                resultado = cantidad * factor
                print(f"{cantidad} {unidad_origen} son {resultado} {unidad_destino}.\n\n")
            else:
                print("Conversión no disponible.")
        case "n":
            print("¡Hasta luego!")
            break

        case _:
            print("Por favor, responde con 'sí' o 'no'.")
