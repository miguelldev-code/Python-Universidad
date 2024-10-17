# iterar significa recorrer cada elemento de un conjunto de datos


# BREAK
cadena = "Texto"
for letra in cadena:
    print(letra)
    break
else:
    print("Fin del ciclo") # No se ejecuta

# CONTINUE
for i in range(6):
    if i %  2 != 0:
        continue
    print(f"Valor: {i}")
