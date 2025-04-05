""" Enunciado:
    Una tienda tiene una lista de productos disponibles. 
    Cada vez que se vende un producto, debe ser eliminado 
    de la lista. El proceso se repite hasta que el usuario 
    escriba "fin". Al final, se muestra el stock restante.

Pasos:

    1. Crear una lista con algunos productos iniciales.
    2. Pedir al usuario que ingrese el nombre del producto vendido.
    3. Si el producto está en la lista, eliminarlo.
    4. Si no está en la lista, mostrar un mensaje de error.
    5. Repetir el proceso hasta que el usuario escriba "fin".
    6. Mostrar los productos restantes en la tienda.
"""


productos = ["arroz", "azúcar", "café", "leche", "pan"]  

while True:  
    print("Stock actual:", productos)  
    vendido = input("Producto vendido (escribe 'fin' para salir): ").lower()  
    if vendido == "fin":  
        break  
    if vendido in productos:  
        productos.remove(vendido)  
        print(f"Se ha vendido {vendido}.")  
    else:  
        print("Ese producto no está en stock.")  

print("Stock final:", productos)  
