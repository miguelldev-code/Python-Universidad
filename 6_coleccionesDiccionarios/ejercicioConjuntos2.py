# Dada una lista con elementos duplicados, crea una nueva lista sin los duplicados.

# Lista con elementos duplicados
numeros = [1, 2, 2, 3, 4, 4, 5]

# Usamos un conjunto para eliminar duplicados y luego lo convertimos de nuevo en lista
numeros_unicos = list(set(numeros))

print("Lista sin duplicados:", numeros_unicos)


