# Escriba un programa que permita al usuario ingresar una serie de numeros.
# El programa debe detenerse si el usuario ingresa el numero -1.
# Adicionalmente, si el usuario ingresa un numero negativo distinto de -1,
# el programa debe ignorarlo y continuar pidiendo numeros.
# Al final, el programa mostrara la suma de los numeros ingresados (sin contar el -1).

# INICIALIZAR VARIABLES
suma = 0

while True:
    # PEDIR AL USUARIO UN NUMERO
    numero = int(input("Ingresa un numero (-1 para salir): "))
    
    # CONDICION DE SALIDA
    if numero == -1:
        break  # Termina el bucle si el usuario ingresa -1
    
    # IGNORAR NUMEROS NEGATIVOS DISTINTOS DE -1
    if numero < 0:
        print("Numero negativo ignorado.")
        continue  # Salta el resto del codigo en la iteracion actual
    
    # ACUMULAR LA SUMA
    suma += numero

# MOSTRAR RESULTADO FINAL
print(f"La suma de los numeros ingresados es: {suma}")
