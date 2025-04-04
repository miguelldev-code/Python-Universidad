"""
Definir una lista de listas (matriz) que contenga información sobre empleados.
con tres campos: nombre, edad y cargo.

Luego, imprimir la lista de empleados con su información formateada.

# Salida
Nombre: Juan, Edad: 30, Cargo: Gerente

"""


empleados = [
    ["Juan", 30, "Gerente"],
    ["María", 25, "Analista"],
    ["Carlos", 28, "Desarrollador"],
    ["Ana", 22, "Diseñadora"],
]

print("Lista de empleados:")
for empleado in empleados:
    print(f"Nombre: {empleado[0]}, Edad: {empleado[1]}, Cargo: {empleado[2]}")
