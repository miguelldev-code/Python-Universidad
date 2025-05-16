class Persona:
    # Lista de nacionalidades válidas (atributo de clase)
    nacionalidades_validas = ["Mexicana", "Española", "Argentina"]

    def __init__(self, nombre, edad, nacionalidad):
        # Atributos de instancia (privados por convención)
        self._nombre = nombre
        self._edad = edad
        self.nacionalidad = nacionalidad  # Atributo público

    # Método de instancia
    def presentarse(self):
        return f"Soy {self._nombre}, tengo {self._edad} años y soy {self.nacionalidad}"

    # Getter para nombre (property)  
    @property
    def nombre(self):
        return self._nombre.upper()  # Devuelve el nombre en mayúsculas

    # Setter para nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        self._nombre = nuevo_nombre

    # Getter para edad
    @property
    def edad(self):
        return self._edad

    # Setter para edad con validación
    @edad.setter
    def edad(self, nueva_edad):
        if not isinstance(nueva_edad, int) or nueva_edad < 0:
            raise ValueError("La edad debe ser un número entero positivo")
        self._edad = nueva_edad

    # Método estático
    @staticmethod
    def es_nacionalidad_valida(nacionalidad):
        return nacionalidad in Persona.nacionalidades_validas
