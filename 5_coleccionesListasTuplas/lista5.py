"""Enunciado:
El usuario ingresará los nombres completos (nombre y apellido) de 3 personas. 
El programa debe separar los nombres y apellidos, almacenarlos en listas 
diferentes y mostrarlos por separado.

Pasos:

    1. Crear tres listas vacías: una para los nombres completos, otra para 
       los nombres y otra para los apellidos.
    2. Pedir al usuario que ingrese el nombre completo (nombre y apellido) 
       de 3 personas.
    3. Separar el nombre y el apellido de cada entrada y almacenarlos en 
       las listas correspondientes. NOTA: para los usa " ".join(partes[1:])
    4. Mostrar por separado las listas de nombres y apellidos.
"""

nombres_completos = []  
nombres = []  
apellidos = []  

for _ in range(3):  
    nombre_completo = input("Ingrese nombre y apellido: ")  
    nombres_completos.append(nombre_completo)  
    partes = nombre_completo.split()  
    nombres.append(partes[0])  
    apellidos.append(" ".join(partes[1:]))  

print("Nombres:", nombres)  
print("Apellidos:", apellidos)  
