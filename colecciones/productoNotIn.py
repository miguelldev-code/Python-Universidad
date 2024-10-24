# Programa que verifica la disponibilidad de productos en el inventario.
# Compara una lista de solicitudes con los productos del inventario.
# Si algún producto solicitado no está en el inventario, se agrega a una lista de productos faltantes.
# Al final, si hay productos faltantes, los muestra; si no, informa que todos los productos están disponibles.


# Lista de productos disponibles en el inventario

# Lista de productos solicitados

# Lista vacía para almacenar los productos que no están en el inventario

# Bucle para verificar cada producto solicitado

# Si el producto no está en el inventario, se agrega a la lista de faltantes

# Verificar si hay productos faltantes y mostrar el resultado


# Lista de productos disponibles en el inventario
inventario = ["laptop", "ratón", "teclado", "monitor"]

# Lista de productos solicitados
solicitudes = ["ratón", "teclado", "impresora"]

# Lista vacía para almacenar los productos que no están en el inventario
productos_faltantes = []

# Bucle para verificar cada producto solicitado
for producto in solicitudes:
    # Si el producto no está en el inventario, se agrega a la lista de faltantes
    if producto not in inventario:
        productos_faltantes.append(producto)

# Verificar si hay productos faltantes y mostrar el resultado
if len(productos_faltantes) > 0:
    print("Productos faltantes:", productos_faltantes)
else:
    print("Todos los productos solicitados están disponibles.")