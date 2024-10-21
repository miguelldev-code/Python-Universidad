# Crear la lista de productos
productos = ["manzana", "banana", "naranja", "uva"]
print("Lista original:", productos)

# Agregar un nuevo producto
productos.append("piña")
print("Después de agregar 'piña':", productos)

# Modificar el segundo producto
productos[1] = "mango"
print("Después de modificar 'banana' por 'mango':", productos)

# Eliminar el último producto
productos.pop()
print("Después de eliminar el último producto:", productos)
