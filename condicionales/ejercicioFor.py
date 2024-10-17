# iterar significa recorrer cada elemento de un conjunto de datos

#                   BREAK
# Sale del bucle inmediatamente, sin importar si la 
# condición sigue siendo verdadera.
cadena = "Texto"
for letra in cadena:
    print(letra)
    break
else:
    print("Fin del ciclo") # No se ejecuta

#               CONTINUE

# Salta el resto del código en la iteración 
# actual y pasa a la siguiente iteración.
for i in range(1, 6):
    if i == 3: #Se salta el 3
        continue
    print(i)
