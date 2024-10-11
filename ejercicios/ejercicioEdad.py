# Pedir edad yy decir si es mayor a 18

edad = int(input("Ingrese la edad: "))

if edad >= 18:
    print(f"Tiene {edad} años, por lo que es mayor de edad")
else:
    print(f"Tiene {edad} años, por lo que es menor de edad")