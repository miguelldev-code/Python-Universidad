# Eliminar duplicados de una lista ingresada por el usuario

# Lista vacía para almacenar los valores ingresados por el usuario
lista_usuario = []

# Pedir al usuario que ingrese valores hasta que escriba "fin"
while True:
    valor = input("Ingresa un valor (escribe 'fin' para terminar): ")
    
    if valor == "fin":
        break  # Detener el bucle cuando el usuario escriba 'fin'
    
    lista_usuario.append(valor)  # Agregar el valor ingresado a la lista

# Crear una nueva lista sin duplicados
lista_sin_duplicados = []

for valor in lista_usuario:
    if valor not in lista_sin_duplicados:
        lista_sin_duplicados.append(valor)

# Mostrar la lista original y la lista sin duplicados
print("Lista original:", lista_usuario)
print("Lista sin duplicados:", lista_sin_duplicados)
