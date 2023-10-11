# Escriba una función de Python para calcular el factorial de un número (un entero no negativo). La función acepta el número como argumento
def factorial(numero):
    
    if numero == 0:
        return 1
    
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado
2

numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("El número debe ser no negativo.")
else:
    resultado = factorial(numero)
    print("El factorial de", numero, "es:", resultado)




