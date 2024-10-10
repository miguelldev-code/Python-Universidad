# Pedir numero y que diga si 
# si esta en el rango entre 
# 0 y 5 

numero = int(input("Ingresa el numero: "))

if numero >= 0 and numero <= 5:
    print(f"El numero {numero} esta dentro del rango")
else:
    print(f"El numero {numero} no esta dentro del rango")