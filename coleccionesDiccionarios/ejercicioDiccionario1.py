# Par clave-valor en diccionarios:
# Cada elemento en un diccionario está compuesto por una clave y un valor.
# Ejemplo: En el par "nombre": "Juan", "nombre" es la clave y "Juan" es el valor.

# Estructura de un diccionario:
# Los diccionarios se definen con llaves {}.
# Cada par clave-valor se separa por comas y cada clave se asocia a su valor con dos puntos :.

estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Acceso directo a un valor usando su clave
print(estudiante["nombre"])  # Output: Juan

# Acceso a un valor con get():
# Si la clave no existe, get() devuelve un valor predeterminado (en este caso, "No especificado").
print(estudiante.get("promedio", "No especificado"))  # Output: No especificado
