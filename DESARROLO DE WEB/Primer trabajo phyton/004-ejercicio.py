# Programa que permita calcular la edad de una persona conociendo el año actual y el usuario digita su año de nacimiento en python

anioactual = int(input("Ingrese el año actual: "))
anionacimiento = int(input("Ingrese su fecha de nacimiento: "))


edad = anioactual - anionacimiento
print(f" Tienes {edad} años de edad. ")