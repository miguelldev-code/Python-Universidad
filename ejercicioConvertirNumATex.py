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