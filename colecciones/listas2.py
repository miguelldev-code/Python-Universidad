#           METODOS DE LISTAS

# Crear la lista de productos
productos = ["manzana", "banana", "naranja", "uva"]
print("Lista original:", productos)

# 1. Agregar un nuevo producto al final de la lista (append)
productos.append("piña")
print("Después de agregar 'piña':", productos)

# 2. Modificar el segundo producto
productos[1] = "mango"
print("Después de modificar 'banana' por 'mango':", productos)

# 3. Eliminar el último producto (pop)
productos.pop()
print("Después de eliminar el último producto:", productos)

# 4. Insertar un producto en una posición específica (insert)
productos.insert(2, "pera")  # Insertar 'pera' en la posición 2 (tercer lugar)
print("Después de insertar 'pera' en la posición 2:", productos)

# 5. Extender la lista con múltiples productos (extend)
productos.extend(["kiwi", "fresa"])  # Agregar varios productos al final
print("Después de extender la lista con 'kiwi' y 'fresa':", productos)

# 6. Eliminar un producto específico por su valor (remove)
productos.remove("naranja")  # Elimina la primera aparición de 'naranja'
print("Después de eliminar 'naranja':", productos)

# 7. Ordenar la lista alfabéticamente (sort)
productos.sort()
print("Después de ordenar la lista:", productos)

# 8. Invertir el orden de los elementos de la lista (reverse)
productos.reverse()
print("Después de invertir el orden de la lista:", productos)

# 9. Contar cuántas veces aparece un elemento en la lista (count)
cantidad_manzanas = productos.count("manzana")
print(f"La cantidad de 'manzana' en la lista es: {cantidad_manzanas}")

# 10. Encontrar el índice de un producto en la lista (index)
indice_uva = productos.index("uva")
print(f"El índice de 'uva' en la lista es: {indice_uva}")
