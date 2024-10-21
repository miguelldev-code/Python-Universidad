# Contar elementos en una lista
# Dada una lista de números, cuenta cuántos 
# son mayores que 10.

# Lista de números
numeros = [4, 11, 32, 8, 15, 6, 23]

# Contador para números mayores que 10
contador = 0

# Recorrer la lista y contar cuántos son mayores que 10
for numero in numeros:
    if numero > 10:
        contador += 1

print(f"Hay {contador} números mayores que 10.")
