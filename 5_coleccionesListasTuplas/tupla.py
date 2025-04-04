"""

Enunciado:
En un teatro, los asientos están organizados por filas y números. 
Se almacenan en una lista de tuplas y se debe verificar si un asiento 
está disponible para su reserva.

Pasos:

    Crear una lista con tuplas que representen los asientos disponibles (fila, número).

    Mostrar los asientos disponibles.

    Pedir al usuario que ingrese una fila y un número de asiento.

    Verificar si el asiento está en la lista y eliminarlo si es reservado.

    Si no está disponible, mostrar un mensaje de error.

    """
asientos_disponibles = [("A", 1), ("A", 2), ("B", 1), ("B", 2), ("C", 1), ("C", 2)]

print("Asientos disponibles:", asientos_disponibles)
while True:
    cantidad_asientos = int(input("Ingrese la cantidad de asientos a reservar: "))
    if cantidad_asientos <= len(asientos_disponibles):
        break
    else:
        print("No hay suficientes asientos disponibles. Intente nuevamente.")



for _ in range(cantidad_asientos):
    fila = input("Ingrese la fila del asiento que desea reservar: ").upper()
    numero = int(input("Ingrese el número del asiento: "))

    asiento = (fila, numero)
    if asiento in asientos_disponibles:
        asientos_disponibles.remove(asiento)
        print(f"Asiento {asiento} reservado con éxito.")
    else:
        print("El asiento no está disponible o no existe.")

print("Asientos restantes:", asientos_disponibles)
