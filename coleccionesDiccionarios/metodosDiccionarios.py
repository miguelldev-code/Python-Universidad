# Diccionario de ejemplo
persona = {"nombre": "Ana", "edad": 28}

# get()
# Obtiene el valor de una clave especificada. Permite agregar un valor predeterminado si la clave no existe.
print(persona.get("nombre"))  # Output: Ana
print(persona.get("profesion", "Desconocido"))  # Output: Desconocido

# keys()
# Devuelve una vista de todas las claves del diccionario, útil para iterar sobre ellas.
print(persona.keys())  # Output: dict_keys(['nombre', 'edad'])

# values()
# Devuelve una vista de todos los valores en el diccionario, útil para obtener solo los datos almacenados.
print(persona.values())  # Output: dict_values(['Ana', 28])

# items()
# Devuelve una vista de los pares clave-valor como tuplas, ideal para recorrer el diccionario en pares.
print(persona.items())  # Output: dict_items([('nombre', 'Ana'), ('edad', 28)])

# update()
# Actualiza el diccionario con otro diccionario, agregando o modificando las claves y valores según el contenido del nuevo diccionario.
info_adicional = {"profesion": "Ingeniera"}
persona.update(info_adicional)
print(persona)  # Output: {'nombre': 'Ana', 'edad': 28, 'profesion': 'Ingeniera'}
