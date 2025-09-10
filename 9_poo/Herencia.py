class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"{self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        print(f"{self.marca} {self.modelo} se ha detenido.")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llama al constructor de Vehiculo
        self.num_puertas = num_puertas

    def abrir_puertas(self):
        print(f"Abriendo {self.num_puertas} puertas.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_manillar):
        super().__init__(marca, modelo)
        self.tipo_manillar = tipo_manillar

    def hacer_caballito(self):
        print("¡La moto está haciendo un caballito!")

# Crear objetos
mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Moto("Harley-Davidson", "Sportster", "Alto")

# Métodos heredados
mi_coche.arrancar()  # Salida: Toyota Corolla ha arrancado.
mi_moto.detener()    # Salida: Harley-Davidson Sportster se ha detenido.

# Métodos propios
mi_coche.abrir_puertas()      # Salida: Abriendo 4 puertas.
mi_moto.hacer_caballito()     # Salida: ¡La moto está haciendo un caballito!