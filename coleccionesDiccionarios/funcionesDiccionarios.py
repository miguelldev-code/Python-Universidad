# Ejemplo de uso de diccionarios en Python

# 1. Almacenar datos relacionados con etiquetas
usuario = {
    "nombre": "María",
    "edad": 28,
    "email": "maria@example.com"
}
print(usuario["nombre"])  # Output: María

# 2. Acceso directo a información específica
productos = {
    "manzana": 1.2,
    "banana": 0.5,
    "naranja": 0.8
}
print("Precio de la banana:", productos["banana"])  # Output: 0.5

# 3. Organizar datos de configuración
configuracion = {
    "modo": "oscuro",
    "volumen": 70,
    "resolucion": "1080p"
}
print(configuracion["modo"])  # Output: oscuro

# 4. Relacionar objetos complejos en bases de datos simples
estudiantes = {
    1: {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"},
    2: {"nombre": "Ana", "edad": 22, "carrera": "Matemáticas"}
}
print(estudiantes[1]["nombre"])  # Output: Juan
