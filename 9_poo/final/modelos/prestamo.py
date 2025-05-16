from datetime import datetime, timedelta

class Prestamo:
    # Método estático para calcular fecha de devolución
    @staticmethod
    def calcular_fecha_devolucion(dias=7):
        return datetime.now() + timedelta(days=dias)

    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.calcular_fecha_devolucion()

    def __str__(self):
        return f"Préstamo de {self.libro} a {self.usuario.nombre}. Devolver antes del {self.fecha_devolucion.strftime('%d/%m/%Y')}"
