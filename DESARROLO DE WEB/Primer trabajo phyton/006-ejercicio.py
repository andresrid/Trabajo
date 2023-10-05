# Programa que permita calcular el 30%, el 60% y el 90% de cualquier número
numero = float(input("Ingresa un número: "))

porcentaje_30 = (numero * 30) / 100
porcentaje_60 = (numero * 60) / 100
porcentaje_90 = (numero * 90) / 100


print(f"El 30% de {numero} es {porcentaje_30}")
print(f"El 60% de {numero} es {porcentaje_60}")
print(f"El 90% de {numero} es {porcentaje_90}")