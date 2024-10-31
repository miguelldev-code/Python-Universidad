# Comparar Inventarios de Tiendas

# Saber qué productos tienen ambas tiendas en común.
# Encontrar productos exclusivos de cada tienda.
# Ver todos los productos sin duplicados.

tienda1 = {"manzanas", "naranjas", "bananas", "peras"}
tienda2 = {"bananas", "peras", "uvas", "sandías"}

# Productos en común
productos_comunes = tienda1.intersection(tienda2)
print("Productos en ambas tiendas:", productos_comunes)  
# Output: {'bananas', 'peras'}

# Productos solo en la primera tienda
solo_tienda1 = tienda1.difference(tienda2)
print("Productos solo en tienda 1:", solo_tienda1)
# Output: {'manzanas', 'naranjas'}

# Productos solo en la segunda tienda
solo_tienda2 = tienda2.difference(tienda1)
print("Productos solo en tienda 2:", solo_tienda2)
# Output: {'uvas', 'sandías'}

# Todos los productos sin duplicados
todos_los_productos = tienda1.union(tienda2)
print("Todos los productos:", todos_los_productos)
# Output: {'manzanas', 'naranjas', 'bananas', 'peras', 'uvas', 'sandías'}
