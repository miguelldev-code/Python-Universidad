# Inventario: clave = código del producto, valor = diccionario con detalles
inventario = {
    "A100": {
        "nombre": "Laptop Gamer",
        "precio": 1500,
        "stock": 10,
        "categoria": "Tecnología"
    },
    "B200": {
        "nombre": "Smartphone 5G",
        "precio": 800,
        "stock": 25,
        "categoria": "Tecnología"
    }
}

# --- Operaciones clave con diccionarios ---

# 1) Acceder a valores usando claves
print("Precio del producto A100:", inventario["A100"]["precio"], "$\n")  # Salida: 1500 $

# 2) get() → Evitar KeyError si la clave no existe
stock_b200 = inventario.get("B200", {}).get("stock", 0)
print("Stock de B200:", stock_b200, "\n")  # Salida: 25

stock_fantasma = inventario.get("XYZ", {}).get("stock", 0)
print("Stock de XYZ:", stock_fantasma, "\n")  # Salida: 0

# 3) update() → Modificar múltiples campos de un producto
inventario["A100"].update({"stock": 5, "precio": 1400})
print("A100 actualizado:", inventario["A100"], "\n")

# 4) Agregar nuevo producto (como nuevo par clave-valor)
inventario["C300"] = {
    "nombre": "Tablet 10''",
    "precio": 300,
    "stock": 15,
    "categoria": "Tecnología"
}
print("Producto C300 agregado:", inventario["C300"], "\n")

# 5) pop() → Eliminar producto y obtener sus datos
producto_eliminado = inventario.pop("B200", None)
print("Producto eliminado (B200):", producto_eliminado["nombre"], "\n")

# 6) keys() → Listar códigos de productos
print("Códigos de productos:", inventario.keys(), "\n")

# 7) items() → Iterar sobre todos los productos
print("--- Detalles completos del inventario ---")
for codigo, detalles in inventario.items():
    print(f"{codigo}: {detalles['nombre']} | Stock: {detalles['stock']}")

# 8) Verificar existencia de clave (operador 'in')
print("\n¿Existe el producto A100?", "A100" in inventario)  # True