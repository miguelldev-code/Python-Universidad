nombre = "Usuario1"
# print(nombre)

# Parámetro con valor por defecto
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}!")

saludar()  # Imprime: Hola, Usuario!
saludar("Carlos")  # Imprime: Hola, Carlos!

# print(nombre)    No funciona porque solo se lee el bloque


