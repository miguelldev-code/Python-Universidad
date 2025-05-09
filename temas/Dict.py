def agregar_producto(inventario):
    codigo = input("\nCódigo: ").upper()
    if codigo in inventario:
        print("❌ Ya existe")
        return inventario

    nombre = input("Nombre: ")
    precio = float(input("Precio $: "))
    stock = int(input("Stock: "))
    categoria = input("Categoría: ")

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria
    }
    print(f"✅ {codigo} agregado")
    return inventario

def actualizar_producto(inventario):
    codigo = input("\nCódigo a actualizar: ").upper()
    if codigo not in inventario:
        print("❌ No existe")
        return inventario

    p = inventario[codigo]

    nuevo_nombre = input(f"Nombre ({p['nombre']}): ")
    if nuevo_nombre:
        p["nombre"] = nuevo_nombre

    nuevo_precio = input(f"Precio $({p['precio']}): ")
    if nuevo_precio:
        p["precio"] = float(nuevo_precio)

    nuevo_stock = input(f"Stock ({p['stock']}): ")
    if nuevo_stock:
        p["stock"] = int(nuevo_stock)

    nueva_categoria = input(f"Categoría ({p['categoria']}): ")
    if nueva_categoria:
        p["categoria"] = nueva_categoria

    print(f"✅ {codigo} actualizado")
    return inventario

def eliminar_producto(inventario):
    codigo = input("\nCódigo a eliminar: ").upper()
    if codigo in inventario:
        inventario.pop(codigo)
        print(f"✅ {codigo} eliminado")
    else:
        print("❌ No existe")
    return inventario

def ver_detalles(inventario):
    codigo = input("\nCódigo: ").upper()
    if codigo in inventario:
        p = inventario[codigo]
        print("\n".join([f"{k}: {v}" for k, v in p.items()]))
    else:
        print("❌ No existe")

def listar_productos(inventario):
    print("\n" + "-"*60)
    print(f"{'Código':<8}{'Nombre':<20}{'Precio':<12}{'Stock':<8}{'Categoría':<10}")
    for codigo, p in inventario.items():
        print(f"{codigo:<8}{p['nombre'][:18]:<20}${p['precio']:<11}{p['stock']:<8}{p['categoria']:<10}")

def verificar_existencia(inventario):
    codigo = input("\nCódigo: ").upper()
    if codigo in inventario:
        print("✅ Existe")
    else:
        print("❌ No existe")

def main():
    inventario = {
        "A100": {"nombre": "Laptop Gamer", "precio": 1500.0, "stock": 5, "categoria": "Tecnología"},
        "B200": {"nombre": "Smartphone 5G", "precio": 800.0, "stock": 15, "categoria": "Tecnología"}
    }

    while True:
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

        if opcion == "1":
            inventario = agregar_producto(inventario)
        elif opcion == "2":
            inventario = actualizar_producto(inventario)
        elif opcion == "3":
            inventario = eliminar_producto(inventario)
        elif opcion == "4":
            ver_detalles(inventario)
        elif opcion == "5":
            listar_productos(inventario)
        elif opcion == "6":
            verificar_existencia(inventario)
        elif opcion == "7":
            print("\n¡Hasta luego! 👋")
            break
        else:
            print("\n❌ Opción inválida")

if __name__ == "__main__":
    main()
