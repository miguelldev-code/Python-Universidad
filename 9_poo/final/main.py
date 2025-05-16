from modelos.libro import Libro
from modelos.usuario import Usuario, Estudiante
from modelos.prestamo import Prestamo

def main():
    # Crear datos iniciales
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "123-456")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "789-012")
    usuario = Estudiante("Alexander Lozada", "A001", "Ingeniería")

    # Menú interactivo
    while True:
        print("\n=== BIBLIOTECA UCATÓLICA ===")
        print("1. Prestar libro")
        print("2. Devolver libro")
        print("3. Ver mis libros")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nLibros disponibles:")
            print(f"1. {libro1}")
            print(f"2. {libro2}")
            eleccion = input("Número del libro a prestar: ")
            libro = libro1 if eleccion == "1" else libro2
            prestamo = Prestamo(usuario, libro)
            usuario.tomar_prestado(libro)
            print(prestamo)

        elif opcion == "2":
            if usuario._libros_prestados:
                print("Tus libros prestados:")
                usuario.mostrar_libros()
                eleccion = input("Número del libro a devolver: ")
                libro = libro1 if eleccion == "1" else libro2
                usuario.devolver_libro(libro)
            else:
                print("No tienes libros para devolver.")

        elif opcion == "3":
            usuario.mostrar_libros()

        elif opcion == "4":
            print("¡Gracias por usar la biblioteca!")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
