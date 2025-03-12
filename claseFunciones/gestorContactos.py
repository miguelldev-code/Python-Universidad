"""
Gestor de Contactos en Python  
Este programa permite agregar, buscar, eliminar y mostrar contactos  
usando un diccionario en Python. 
 
Conceptos Técnicos Aprendidos
- Uso de diccionarios para almacenar contactos.
- Funciones para organizar el código.
- Bucle while con un menú interactivo.
- Entrada y salida de datos con input() y print().
"""

# Diccionario para almacenar los contactos
contactos = {}

def agregar_contacto():
    """Agrega un nuevo contacto a la agenda."""
    nombre = input(" Ingrese el nombre del contacto: ")
    telefono = input(" Ingrese el número de teléfono: ")
    correo = input(" Ingrese el correo electrónico: ")
    
    contactos[nombre] = {"Teléfono": telefono, "Correo": correo}
    print(f" Contacto '{nombre}' agregado correctamente.\n")

def buscar_contacto():
    """Busca un contacto por nombre."""
    nombre = input(" Ingrese el nombre del contacto a buscar: ")
    if nombre in contactos:
        print(f" Contacto encontrado: {contactos[nombre]['Teléfono']}  {contactos[nombre]['Correo']}")
    else:
        print(" Contacto no encontrado.\n")

def eliminar_contacto():
    """Elimina un contacto si existe."""
    nombre = input(" Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f" Contacto '{nombre}' eliminado correctamente.\n")
    else:
        print(" Contacto no encontrado.\n")

def mostrar_contactos():
    """Muestra todos los contactos almacenados."""
    if not contactos:
        print(" No hay contactos guardados.\n")
    else:
        print("\n Lista de contactos:")
        for nombre, datos in contactos.items():
            print(f" {nombre} |  {datos['Teléfono']} |  {datos['Correo']}")
        print()

def menu():
    """Menú interactivo para el usuario."""
    while True:
        print("\n **Gestor de Contactos**")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Eliminar Contacto")
        print("4. Mostrar Todos")
        print("5. Salir")

        opcion = input("\nElige una opción (1-5): ")

        match opcion:
            case "1":
                agregar_contacto()
            case "2":
                buscar_contacto()
            case "3":
                eliminar_contacto()
            case "4":
                mostrar_contactos()
            case "5":
                print(" Saliendo del programa...")
                break
            case _:
                print(" Opción no válida, intenta de nuevo.\n")

menu()
