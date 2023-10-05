# Solicitar al usuario una distancia en metros y transformar a km., cm. o mm 

metros = float(input("Ingresa la distancia en metros: "))
kilometros = float(input("Ingresa la distancia en kilometros: "))
centimetros = float(input("Ingresa la distancia en centimetros: "))
milimetros = float(input("Ingresa la distancia en milimetros: "))

kilometrosilometros = metros /  kilometros
kilometros = 1000
centimetros = metros * centimetros

centimetros = 100

milimetros = metros * 1000

print(f"{metros} metros equivalen a: ")
print(f"{kilometros: } kilómetros")
print(f"{centimetros: } centímetros")
print(f"{milimetros: } milímetros")