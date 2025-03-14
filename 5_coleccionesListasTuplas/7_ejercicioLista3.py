# Dada una lista con elementos duplicados, crea una nueva 
# lista sin los duplicados.


# Lista con elementos duplicados
numeros = [1, 2, 2, 3, 4, 4, 5]

# Lista para almacenar los números únicos
numeros_unicos = []

# Recorrer la lista original y agregar solo los elementos únicos
for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)


print("Lista sin duplicados:", numeros_unicos)
