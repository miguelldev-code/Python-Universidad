def obtener_codigo():
    """Función para obtener un código de producto válido del usuario"""
    codigo = input("\nCódigo: ").upper().strip()
    if not codigo:
        raise ValueError("El código no puede estar vacío")
    return codigo

def obtener_nombre():
    """Función para obtener un nombre de producto válido del usuario"""
    nombre = input("Nombre: ").strip()
    if not nombre:
        raise ValueError("El nombre no puede estar vacío")
    return nombre

def obtener_precio():
    """Función para obtener un precio válido del usuario"""
    try:
        precio = float(input("Precio $: "))
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return precio
    except ValueError:
        raise ValueError("El precio debe ser un número válido (ej: 19.99)")

def obtener_stock():
    """Función para obtener un stock válido del usuario"""
    try:
        stock = int(input("Stock: "))
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")
        return stock
    except ValueError:
        raise ValueError("El stock debe ser un número entero válido (ej: 10)")

def obtener_categoria():
    """Función para obtener una categoría válida del usuario"""
    categoria = input("Categoría: ").strip()
    if not categoria:
        raise ValueError("La categoría no puede estar vacía")
    return categoria

def agregar_producto(inventario):
    """Función para agregar un producto al inventario"""
    try:
        codigo = obtener_codigo()

        if codigo in inventario:
            print("❌ Ya existe ese código")
            return inventario

        nombre = obtener_nombre()
        precio = obtener_precio()
        stock = obtener_stock()
        categoria = obtener_categoria()

        inventario[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }
        print(f"✅ {codigo} agregado")

    except ValueError as e:
        print(f"\n⚠ Error: {e}. No se agregó el producto.")
    
    return inventario

def actualizar_producto(inventario):
    """Función para actualizar un producto en el inventario"""
    try:
        codigo = obtener_codigo()

        if codigo not in inventario:
            print("❌ No existe ese producto")
            return inventario

        producto = inventario[codigo]
        
        print("\nDeja vacío para mantener el valor actual:")
        
        # Actualizar nombre
        nuevo_nombre = input(f"Nombre ({producto['nombre']}): ").strip()
        if nuevo_nombre:
            producto["nombre"] = nuevo_nombre
        
        # Actualizar precio
        nuevo_precio = input(f"Precio $({producto['precio']}): ").strip()
        if nuevo_precio:
            try:
                precio = float(nuevo_precio)
                if precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0")
                producto["precio"] = precio
            except ValueError:
                print("⚠ Valor inválido. No se cambió el precio")
        
        # Actualizar stock
        nuevo_stock = input(f"Stock ({producto['stock']}): ").strip()
        if nuevo_stock:
            try:
                stock = int(nuevo_stock)
                if stock < 0:
                    raise ValueError("El stock no puede ser negativo")
                producto["stock"] = stock
            except ValueError:
                print("⚠ Valor inválido. No se cambió el stock")
        
        # Actualizar categoría
        nueva_categoria = input(f"Categoría ({producto['categoria']}): ").strip()
        if nueva_categoria:
            producto["categoria"] = nueva_categoria
        
        print(f"✅ {codigo} actualizado")
        
    except ValueError as e:
        print(f"\n⚠ Error: {e}")
    
    return inventario

def eliminar_producto(inventario):
    """Función para eliminar un producto del inventario"""
    try:
        codigo = obtener_codigo()

        if codigo in inventario:
            inventario.pop(codigo)
            print(f"✅ {codigo} eliminado")
        else:
            print("❌ No existe ese código")
            
    except ValueError as e:
        print(f"\n⚠ Error: {e}")
    
    return inventario

def ver_detalles(inventario):
    """Función para ver los detalles de un producto"""
    try:
        codigo = obtener_codigo()

        if codigo in inventario:
            producto = inventario[codigo]
            print("\nDetalles:")
            for clave, valor in producto.items():
                print(f"- {clave.capitalize()}: {valor}")
        else:
            print("❌ No existe ese código")
            
    except ValueError as e:
        print(f"\n⚠ Error: {e}")

def listar_productos(inventario):
    """Función para listar todos los productos del inventario"""
    print("\n" + "-"*60)
    print(f"{'Código':<8}{'Nombre':<20}{'Precio':<12}{'Stock':<8}{'Categoría':<10}")
    for codigo, p in inventario.items():
        print(f"{codigo:<8}{p['nombre'][:18]:<20}${p['precio']:<11}{p['stock']:<8}{p['categoria']:<10}")

def verificar_existencia(inventario):
    """Función para verificar si un producto existe en el inventario"""
    try:
        codigo = obtener_codigo()

        if codigo in inventario:
            print("✅ Existe")
        else:
            print("❌ No existe")
        
    except ValueError as e:
        print(f"\n⚠ Error: {e}")

def main():
    """Función principal que gestiona el sistema de inventario"""
    inventario = {
        "A100": {"nombre": "Laptop Gamer", "precio": 1500.0, "stock": 5, "categoria": "Tecnología"},
        "B200": {"nombre": "Smartphone 5G", "precio": 800.0, "stock": 15, "categoria": "Tecnología"}
    }

    while True:
        try:
            opcion = input("\n" + "="*30 + """
SISTEMA DE INVENTARIO
1. Agregar producto
2. Actualizar producto
3. Eliminar producto
4. Ver detalles
5. Listar todos
6. Verificar existencia
7. Salir
Opción (1-7): """)

            match opcion:
                case "1": inventario = agregar_producto(inventario)
                case "2": inventario = actualizar_producto(inventario)
                case "3": inventario = eliminar_producto(inventario)
                case "4": ver_detalles(inventario)
                case "5": listar_productos(inventario)
                case "6": verificar_existencia(inventario)
                case "7": print("\n¡Hasta luego! 👋"); break
                case _: print("\n❌ Opción inválida. Usa números del 1 al 7")
                
        except Exception as e:
            print(f"\n⚠ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()