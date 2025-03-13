# crear un programa que pida la edad y muestre si la persona es 
# menor de edad, adulta o mayor de 60 años.

edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 60:
    print("Eres adulto.")
else:
    print("Eres mayor de 60 años.")
