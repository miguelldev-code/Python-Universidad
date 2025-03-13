# El if-else permite tomar decisiones según una condición.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


# Si tenemos multiples condiciones

nota = float(input("Ingrese su calificación: "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprobado")
else:
    print("Reprobado")

# Operador de comparacion

numero = int(input("Digite un numero entre 1 y 3: "))
numeroTexto = ""

if numero == 1:
    numeroTexto = "Numero 1"
elif numero == 2:
    numeroTexto = "Numero 2"
elif numero == 3:
    numeroTexto = "Numero 3"
else:
    numeroTexto = "Numero fuera de rango"

print(f"Seleccionaste el {numero} - {numeroTexto}")
print(type(numero))
print(type(numeroTexto))