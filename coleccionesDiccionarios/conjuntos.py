# Sintaxis para definir diferentes tipos de colecciones en Python

# 1. Conjuntos vacíos (Set)
# Un conjunto vacío se define usando `set()`, no `{}`, ya que `{}` crea un diccionario vacío.
b = set()
print(type(b))  # Output: <class 'set'>

# 2. Listas
# Son mutables (se pueden modificar después de su creación), y permiten acceder a los elementos por medio de índices.
# Ejemplo de lista:
usuario = ["Juan", "juan", "1234"]
print(type(usuario))  # Output: <class 'list'>

# 3. Tuplas
# Son inmutables (no se pueden modificar después de su creación) y también permiten el acceso por índices.
usuario = ("Juan", "juan", "1234")
print(type(usuario))  # Output: <class 'tuple'>

# 4. Conjuntos (Set)
# Son mutables, pero NO permiten acceder a sus elementos por índice y no tienen un orden específico.
# Son útiles para almacenar datos únicos y realizar operaciones de pertenencia o comparación.
usuario = {"Juan", "juan", "1234"}
print(type(usuario))  # Output: <class 'set'>



# Ejemplo de uso de conjuntos (Set):
# Para evitar elementos duplicados y trabajar con operaciones de conjuntos, como unión, intersección, etc.

# Crear un conjunto usando llaves {} o la función set()
frutas = {"manzana", "banana", "naranja"}
# O también se puede crear un conjunto a partir de una lista con `set()`
frutas = set(["manzana", "banana", "naranja"])



# 5. Agregar y eliminar elementos en un conjunto
# Método `add`: Añade un elemento al conjunto
frutas.add("pera")
print(frutas)  # Output: {'manzana', 'banana', 'naranja', 'pera'}

# Método `remove`: Elimina un elemento del conjunto. Da error si el elemento no está presente.
frutas.remove("banana")
print(frutas)  # Output: {'manzana', 'naranja', 'pera'}

# Método `discard`: Similar a `remove`, pero no da error si el elemento no está presente.
frutas.discard("banana")  # No hace nada porque "banana" ya fue removida
print(frutas)  # Output: {'manzana', 'naranja', 'pera'}


