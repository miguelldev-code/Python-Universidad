# Crear una tupla de ciudades
tupla_ciudades = ("Madrid", "París", "Roma", "Berlín", "Lisboa")

# Pedir al usuario una ciudad para buscar
ciudad = input("Ingresa el nombre de una ciudad: ")

# Comprobar si la ciudad está en la tupla
if ciudad in tupla_ciudades:
    print(f"La ciudad {ciudad} está en la lista.")
else:
    print(f"La ciudad {ciudad} no está en la lista.")
