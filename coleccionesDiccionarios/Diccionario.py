# Par clave-valor: Cada elemento tiene dos partes: una clave y un valor. Por ejemplo, en el par nombre: "Juan", "nombre" es la clave y "Juan" es el valor.

# Estructura de un Diccionario: Los diccionarios se definen usando llaves {}. Dentro, los pares clave-valor están separados por comas, y cada clave se separa de su valor con dos puntos :.

estudiante = {
    "nombre": "Juan",
    "edad": 20,
    "carrera": "Ingeniería"
}


# structura de un Diccionario: Los diccionarios se definen usando llaves {}. Dentro, los pares clave-valor están separados por comas, y cada clave se separa de su valor con dos puntos :.
print(estudiante["nombre"])  # Output: Juan

#   Acceso a Valores: Puedes acceder al valor de un diccionario usando la clave correspondiente entre corchetes [].

print(estudiante.get("promedio", "No especificado"))  # Output: No especificado


