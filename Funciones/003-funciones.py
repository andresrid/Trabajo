# Escriba una función de Python para sumar todos los números de una lista. Lista de muestras: (8, 2, 3, 0, 7)Resultado esperado: 20.
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma


lista_muestra = [8, 2, 3, 0, 7]

resultado = sumar_lista(lista_muestra)

print("Su resultado es:", resultado)