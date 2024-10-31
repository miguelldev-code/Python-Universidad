# Sintaxis

b = set()
print(type(b))

usuario = {"Juan", "juan", "1234"}
print(type(usuario))

usuario = ["Juan", "juan", "1234"]
print(type(usuario))

usuario = ("Juan", "juan", "1234")
print(type(usuario))

# usar la función set() o las llaves {}.

frutas = {"manzana", "banana", "naranja"}
frutas = set(["manzana", "banana", "naranja"])


# Agregar y Eliminar Elementos

frutas.add("pera")
print(frutas)
frutas.remove("banana")
print(frutas)
frutas.discard("banana")
print(frutas)

# Unión de Conjuntos

A = {1, 2, 3}
B = {3, 4, 5}
C = A | B  # o A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}

# Intersección de Conjuntos, en comun

C = A & B  # o A.intersection(B)
print(C)  # Output: {3}

# Diferencia de Conjuntos, diferentes entre a en b

C = A - B  # o A.difference(B)
print(C)  # Output: {1, 2}

# Diferencia Simétrica

C = A ^ B  # o A.symmetric_difference(B), todos los que no se repitan
print(C)  # Output: {1, 2, 4, 5}

