# Sintaxis

# usar la función set() o las llaves {}.

frutas = {"manzana", "banana", "naranja"}
frutas = set(["manzana", "banana", "naranja"])


# Agregar y Eliminar Elementos

frutas.add("pera")
frutas.remove("banana")
frutas.discard("banana")

# Unión de Conjuntos

A = {1, 2, 3}
B = {3, 4, 5}
C = A | B  # o A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}

# Intersección de Conjuntos

C = A & B  # o A.intersection(B)
print(C)  # Output: {3}

# Diferencia de Conjuntos

C = A - B  # o A.difference(B)
print(C)  # Output: {1, 2}

# Diferencia Simétrica

C = A ^ B  # o A.symmetric_difference(B)
print(C)  # Output: {1, 2, 4, 5}

