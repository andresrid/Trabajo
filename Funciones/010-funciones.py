# Escriba una función de Python que tome un número como parámetro y verifique que el número sea primo o no. Un número primo (o primo) es un número natural mayor que 1 y que no tiene divisores positivos aparte de 1 y sí mismo
def es_primo(numero):
    if numero <= 1:
        return False 

    if numero <= 3:
        return True 

    if numero % 2 == 0 or numero % 3 == 0:
        return False  

    
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

numero = 17
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")