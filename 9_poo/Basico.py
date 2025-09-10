class Perro:
    # Constructor (inicializa atributos)
    def __init__(mascota, nombre, edad):
        mascota.nombre = nombre  # Atributo de instancia
        mascota.edad = edad

    # Método
    def ladrar(mascota):
        print(f"{mascota.nombre} dice: ¡Guau!")

# Crear objeto
mi_perro = Perro("Rex", 3)
mi_perro.ladrar()  # Salida: Rex dice: ¡Guau!


class Producto:
    def __init__(self, descripcion, cantidad):
        self.descripcion = descripcion
        self.cantidad= cantidad

    def mostrar_info(self):
        print(f"Producto: {self.descripcion}, Cantidad: {self.cantidad}")

    def stock(self):
        return self.cantidad <= 3
    
producto1 = Producto("Jabon", 20)
producto2 = Producto("Shampoo", 2)

print(producto1.descripcion)
print(producto2.descripcion)
print(producto1.stock())
print(producto2.stock())