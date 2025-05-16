class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id = id_usuario
        self._libros_prestados = []  # Encapsulación: lista protegida

    @property
    def nombre(self):
        return self._nombre

    def tomar_prestado(self, libro):
        if libro.disponible:
            self._libros_prestados.append(libro)
            libro.marcar_prestado()
        else:
            print("No se puede prestar el libro.")

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)
            libro.marcar_devuelto()
        else:
            print("Este libro no fue prestado por ti.")

    def mostrar_libros(self):
        if not self._libros_prestados:
            print("No tienes libros prestados.")
        for libro in self._libros_prestados:
            print(f"- {libro}")

# Herencia: Estudiante es un tipo de Usuario
class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario, carrera):
        super().__init__(nombre, id_usuario)
        self.carrera = carrera

    def __str__(self):
        return f"Estudiante: {self.nombre} ({self.carrera})"
