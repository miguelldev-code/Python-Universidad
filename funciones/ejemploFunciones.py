# Parámetro con valor por defecto
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}!")

saludar()  # Imprime: Hola, Usuario!
saludar("Carlos")  # Imprime: Hola, Carlos!
    
# Uso de *args y **kwargs
def mostrar_datos(*args, **kwargs):
    print("Argumentos posicionales:", args)
    print("Argumentos nombrados:", kwargs)

mostrar_datos(1, 2, 3, nombre="Ana", edad=30)
# Imprime:
# Argumentos posicionales: (1, 2, 3)
# Argumentos nombrados: {'nombre': 'Ana', 'edad': 30}
