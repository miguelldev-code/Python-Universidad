# Ejemplo de listas dentro de diccionarios
# Aquí, cada clave del diccionario contiene una lista de nombres de estudiantes.

estudiantes = {
    "grupo1": ["Ana", "Carlos", "Luis"],
    "grupo2": ["María", "José", "Sara"],
    "grupo3": ["Miguel", "Lucía", "Pablo"]
}

# Acceso a un elemento específico dentro de una lista en el diccionario:
# Se usa la clave para acceder al grupo y luego el índice para seleccionar el nombre.
print(estudiantes["grupo3"][0])  # Output: Miguel

# Recorrer el diccionario para mostrar cada grupo y sus miembros
for grupo, nombres in estudiantes.items():
    print(f"{grupo}: {nombres}")

# Ejemplo de salida:
# grupo1: ['Ana', 'Carlos', 'Luis']
# grupo2: ['María', 'José', 'Sara']
# grupo3: ['Miguel', 'Lucía', 'Pablo']
