# Escriba un programa Python para imprimir los números pares de una lista determinada.
def imprimir_numeros_pares(lista):
    for numero in lista:
        if numero % 2 == 0:
            print(numero)


mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares en la lista:")
imprimir_numeros_pares(mi_lista)