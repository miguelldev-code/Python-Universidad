# pregunte al usuario su edad y muestre por pantalla 
# todos los años que ha cumplido (desde 1 hasta su edad)

edad = int(input("Ingrese la edad: "))

# La funcion range mientras no se especifique un inicio, 
# siempre sera 0

for i in range(edad):
    print(i+1)

