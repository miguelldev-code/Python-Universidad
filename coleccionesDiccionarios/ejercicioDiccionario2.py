# Listas en diccionarios

estudiantes = {
    "grupo1": ["Ana", "Carlos", "Luis"],
    "grupo2": ["María", "José", "Sara"],
    "grupo3": ["Miguel", "Lucía", "Pablo"]
}

print(estudiantes["grupo3"][0])

for grupo, nombres in estudiantes.items():
    print(f"{grupo}: {nombres}")
