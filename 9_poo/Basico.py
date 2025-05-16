class Perro:
    # Constructor (inicializa atributos)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    # Método
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Crear objeto
mi_perro = Perro("Rex", 3)
mi_perro.ladrar()  # Salida: Rex dice: ¡Guau!
