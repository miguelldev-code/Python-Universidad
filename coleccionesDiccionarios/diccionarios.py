# Ejemplo de Conjuntos (set) y Diccionarios en Python

# Conjuntos (set)
# - Estructura de datos mutable (podemos agregar o eliminar elementos).
# - No admite duplicados: todos los elementos deben ser únicos.
# - Acceso por métodos como add, remove y union (no se accede por índice).
# - No tiene posiciones fijas, el orden de los elementos no está garantizado.

# Ejemplo de un conjunto
usuarios_set = {"Juan", "María", "Carlos"}
print(type(usuarios_set))  # Salida: <class 'set'>
print(usuarios_set)

# Diccionarios (dict)
# - Estructura de datos mutable, permite agregar, modificar o eliminar elementos.
# - Organización basada en pares clave-valor, ideal para estructurar datos relacionados.
# - Acceso rápido a valores mediante claves específicas (no por índice).
# - No tiene un orden específico en versiones anteriores a Python 3.7 (en adelante, mantiene el orden de inserción).

# Ejemplo de un diccionario
usuario = {"usuario": "Juan", "email": "juan@example.com", "edad": 25}
print(type(usuario))  # Salida: <class 'dict'>
print(usuario)


