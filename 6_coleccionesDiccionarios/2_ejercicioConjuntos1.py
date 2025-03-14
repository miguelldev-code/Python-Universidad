# Gestión de Inscripciones en Actividades

# Registrar los estudiantes que participan en cada actividad.
# Identificar los estudiantes que están en varias actividades.
# Encontrar estudiantes únicos que solo están en una actividad.
# Encontrar estudiantes que no están inscritos en ninguna actividad.

# Conjuntos de estudiantes inscritos en cada actividad
futbol = {"Ana", "Carlos", "Juan", "Marta", "Luis"}
danza = {"Ana", "Elena", "Marta", "Luis", "Raquel"}
ajedrez = {"Carlos", "Raquel", "Luis", "Jorge"}

# 1. Encontrar estudiantes que participan en más de una actividad (intersección)
multi_actividades = (futbol & danza) | (futbol & ajedrez) | (danza & ajedrez)
print("Estudiantes en múltiples actividades:", multi_actividades)

# 2. Encontrar estudiantes únicos que solo están en una actividad (diferencia)
solo_futbol = futbol - danza - ajedrez
solo_danza = danza - futbol - ajedrez
solo_ajedrez = ajedrez - futbol - danza
print("Estudiantes solo en futbol:", solo_futbol)
print("Estudiantes solo en danza:", solo_danza)
print("Estudiantes solo en ajedrez:", solo_ajedrez)

# 3. Encontrar todos los estudiantes en alguna actividad (unión)
todos_estudiantes = futbol | danza | ajedrez
print("Todos los estudiantes inscritos:", todos_estudiantes)

# 4. Suponiendo que tenemos un conjunto con todos los estudiantes de la universidad
todos_universidad = {"Ana", "Carlos", "Juan", "Marta", "Luis", "Elena", "Raquel", "Jorge", "Sofia", "Miguel"}
sin_actividad = todos_universidad - todos_estudiantes
print("Estudiantes sin actividad:", sin_actividad)
