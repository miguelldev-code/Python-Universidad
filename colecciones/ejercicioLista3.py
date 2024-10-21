#Dada una lista con elementos duplicados, crea una nueva lista sin los duplicados.


# Lista con elementos duplicados
numeros = [1, 2, 2, 3, 4, 4, 5]

# Lista para almacenar los números únicos
numeros_sin_duplicados = []

# Recorrer la lista original y agregar solo los elementos únicos
for numero in numeros:
    if numero not in numeros_sin_duplicados:
        numeros_sin_duplicados.append(numero)

print("Lista sin duplicados:", numeros_sin_duplicados)
