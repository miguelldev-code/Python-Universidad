class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True  # Atributo protegido

    @property
    def disponible(self):
        return self._disponible

    def marcar_prestado(self):
        if self._disponible:
            self._disponible = False
            print(f"Libro '{self._titulo}' prestado.")
        else:
            print("¡El libro no está disponible!")

    def marcar_devuelto(self):
        self._disponible = True
        print(f"Libro '{self._titulo}' devuelto.")

    def __str__(self):
        return f"'{self._titulo}' por {self._autor} (ISBN: {self._isbn})"
