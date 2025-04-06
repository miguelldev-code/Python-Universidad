"""Enunciado:
El usuario ingresará la cantidad de notas que desea registrar. 
El programa debe permitir ingresar cada nota, validando que esté 
en el rango de 0 a 5. Luego, calculará y mostrará el promedio de 
las notas, la nota más alta y la nota más baja.

Pasos:

    1. Pedir al usuario la cantidad de notas que desea ingresar.
    2. Validar que cada nota ingresada esté en el rango de 0 a 5. 
       Si no lo está, solicitar nuevamente la nota.
    3. Almacenar las notas válidas en una lista.
    4. Calcular el promedio de las notas, la nota más alta y la 
       nota más baja.
    5. Mostrar los resultados al usuario.
"""






cantidadNotas = int(input("Ingrese la cantidad de notas: "))

notas = []

for i in range(cantidadNotas):
    while True:

        nota = float(input(f"Ingrese la nota {i + 1}: "))
        if nota < 0 or nota > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
        else:
            notas.append(nota)
            break 


# Promedio, la nota alta y la nota baja
promedio = sum(notas) / len(notas)
notaAlta = max(notas)
notaBaja = min(notas)
print(f"Promedio: {promedio}, Nota alta: {notaAlta}, Nota baja: {notaBaja}")