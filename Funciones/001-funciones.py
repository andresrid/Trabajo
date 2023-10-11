# Escriba una función de Python para encontrar el máximo de tres números. 
def encontrar_maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = 10
num2 = 5
num3 = 8

maximo = encontrar_maximo(num1, num2, num3)
print("El número máximo es:", maximo)
