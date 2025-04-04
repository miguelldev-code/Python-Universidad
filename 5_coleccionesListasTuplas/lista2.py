"""
Ejercicio:
Crear una lista donde almacene las temperaturas y una tupla con los días de la semana.

las temperaturas seran ingresadas por el usuario y al final se mostrara 
la temperatura más alta, la más baja y el promedio de las temperaturas.

"""



temperaturas = []
#Tupla
dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
for i in range(len(dias)):  
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))  
    temperaturas.append(temp)  


print("Temperatura más alta:", max(temperaturas))  
print("Temperatura más baja:", min(temperaturas))  
print("Temperatura promedio:", sum(temperaturas) / len(temperaturas))  
