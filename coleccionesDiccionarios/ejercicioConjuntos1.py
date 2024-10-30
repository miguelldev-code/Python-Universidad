#Supongamos que tenemos dos listas de estudiantes en diferentes materias, y queremos saber:

#¿Quiénes están inscritos en ambas materias?
#¿Quiénes están inscritos en al menos una materia?
#¿Quiénes están solo en la primera materia y no en la segunda?

matematicas = {"Juan", "Ana", "Luis", "Marta"}
fisica = {"Luis", "Ana", "Carlos"}

# 1. Estudiantes en ambas materias (intersección)
print(matematicas & fisica)  # Output: {'Luis', 'Ana'}

# 2. Estudiantes en al menos una materia (unión)
print(matematicas | fisica)  # Output: {'Juan', 'Ana', 'Luis', 'Marta', 'Carlos'}

# 3. Estudiantes solo en matemáticas (diferencia)
print(matematicas - fisica)  # Output: {'Juan', 'Marta'}
