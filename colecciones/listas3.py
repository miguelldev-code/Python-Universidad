# Lista vacía para almacenar las palabras
palabras = []

# Pedir 5 palabras al usuario
for i in range(5):
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

# Recorrer la lista e imprimir cada palabra en mayúsculas
print("Palabras en mayúsculas:")
for palabra in palabras:
    print(palabra.upper())
