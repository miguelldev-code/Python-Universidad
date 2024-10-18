# iterar significa recorrer cada elemento de un conjunto de datos

#                BREAK

# Sale del bucle inmediatamente, sin importar si la 
# condición sigue siendo verdadera.

#La variable letra toca el valor de cada caracter
#De la variable cadena
cadena = "Texto"
for letra in cadena:
    print(letra)
    break  # Termina el bucle con la primera iteracion
else:
    print("Fin del ciclo") # No se ejecuta

#               CONTINUE

# Salta el resto del código en la iteración 
# actual y pasa a la siguiente iteración.
for i in range(1, 6):
    if i == 3: 
        continue  # Se salta el 3 y continua con la iteracion
    print(i)
