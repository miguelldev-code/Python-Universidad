# Convertir una tupla en lista

# Crear una tupla de nombres
tupla_nombres = ("Ana", "Luis", "Carlos")

# Convertir la tupla en una lista
lista_nombres = list(tupla_nombres)

# Modificar la lista
lista_nombres.append("María")
lista_nombres[1] = "Lucía"

# Convertir la lista de nuevo en tupla
tupla_modificada = tuple(lista_nombres)

# Imprimir la tupla modificada
print("Tupla modificada:", tupla_modificada)
