        
#           Diccionario
persona = {"nombre": "Ana", "Edad": 28}

# get()
# Devuelve el valor de la clave especificada

print(persona.get("nombre"))  # Output: Ana
print(persona.get("profesion", "Desconocido"))  # Output: Desconocido

# keys()
# Devuelve una vista de todas las claves del diccionario.

persona = {"nombre": "Ana", "edad": 28}
print(persona.keys())  # Output: dict_keys(['nombre', 'edad'])

# .values()
# Devuelve una vista de todos los valores en el diccionario.

print(persona.values())  # Output: dict_values(['Ana', 28])

# items()
# Devuelve una vista de los pares clave-valor en forma de tuplas.
print(persona.items())  # Output: dict_items([('nombre', 'Ana'), ('edad', 28)])

# update() 
# Actualiza un diccionario con otro diccionario

infoPersona = {"Profesion":"Ingeniera"}
persona.update(infoPersona)
print(persona)  # Output: {'nombre': 'Ana', 'edad': 30, 'profesion': 'Ingeniera'}