#Almacenar Datos Relacionados con Etiquetas

usuario = {
    "nombre": "María",
    "edad": 28,
    "email": "maria@example.com"
}

#Acceso Directo a Información Específica

print(usuario["nombre"])  # Output: María

#Realizar Búsquedas Rápidas y Eficientes

productos = {
    "manzana": 1.2,
    "banana": 0.5,
    "naranja": 0.8
}
print("Precio de la banana:", productos["banana"])  # Output: 0.5


#Organizar Datos de Configuración

configuracion = {
    "modo": "oscuro",
    "volumen": 70,
    "resolucion": "1080p"
}
print(configuracion["modo"])  # Output: oscuro

#Relacionar Objetos Complejos en Bases de Datos Simples

estudiantes = {
    1: {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"},
    2: {"nombre": "Ana", "edad": 22, "carrera": "Matemáticas"}
}
print(estudiantes[1]["nombre"])  # Output: Juan
