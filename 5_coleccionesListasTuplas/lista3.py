""" Enunciado:
El usuario ingresará los nombres y notas de N estudiantes. 
El programa debe identificar al estudiante con la mejor nota y 
al estudiante con la peor nota.

Pasos:

    Crear dos listas vacías: una para nombres y otra para notas.
    Pedir al usuario que ingrese el nombre y la nota de 5 estudiantes.
    Encontrar la nota más alta y más baja en la lista de notas.
    Mostrar el nombre del estudiante con la mejor y la peor nota.

"""


cantidadEstudiantes = int(input("Cantidad de estudiantes: "))

notas = []  
nombres = []  

for estudiantes in range(cantidadEstudiantes):  
    nombre = input("Nombre del estudiante: ")  
    nota = float(input("Nota de " + nombre + ": "))  
    nombres.append(nombre)  
    notas.append(nota)  

indice_max = notas.index(max(notas))  
indice_min = notas.index(min(notas))  

print(f"Mejor nota: {nombres[indice_max]} con {max(notas)}")  
print(f"Peor nota: {nombres[indice_min]} con {min(notas)}")  
