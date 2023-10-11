# Escriba una función de Python para comprobar si un número cae en un rango determinado
def esta_en_rango(numero, rango_inicio, rango_fin):
    return rango_inicio <= numero <= rango_fin


numero = int(input("Ingrese un número: "))
rango_inicio = int(input("Ingrese el inicio del rango: "))
rango_fin = int(input("Ingrese el final del rango: "))

if esta_en_rango(numero, rango_inicio, rango_fin):
    print(numero, "está en el rango.")
else:
    print(numero, "no está en el rango.")
    


