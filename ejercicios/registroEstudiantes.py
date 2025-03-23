"""        Crea un programa que permita:

    - Agregar un estudiante con nombre y nota.
    - Mostrar todos los estudiantes registrados.
    - Mostrar el estudiante con la mejor nota.
    - Calcular el promedio de notas.                   """


estudiantes = []

while True:
    print("\n Registro de Estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Mejor estudiante")
    print("4. Promedio de notas")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("\nNombre del estudiante: ")
        nota = float(input("Nota del estudiante: "))
        estudiantes.append((nombre, nota))
        print(f" Estudiante {nombre} agregado con nota {nota}.")
    
    elif opcion == "2":
        if estudiantes:
            print("\n Lista de estudiantes:")
            for nombre, nota in estudiantes:
                print(f"- {nombre}: {nota}")
        else:
            print("\n No hay estudiantes registrados.")

    elif opcion == "3":
        if estudiantes:
            mejor = max(estudiantes, key=lambda x: x[1])
            print(f"\n Mejor estudiante: {mejor[0]} con nota {mejor[1]}")
        else:
            print("\n No hay estudiantes registrados.")

    elif opcion == "4":
        if estudiantes:
            promedio = sum(nota for _, nota in estudiantes) / len(estudiantes)
            print(f"\n Promedio de notas: {promedio:.2f}")
        else:
            print("\n No hay estudiantes registrados.")

    elif opcion == "5":
        print("\nGracias por usar el sistema. ¡Hasta luego! ")
        break

    else:
        print("\n Opción no válida, intenta de nuevo.")
