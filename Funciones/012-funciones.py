# Escriba una función de Python que compruebe si una cadena pasada es palíndromo o no. Una palabra o frase que es palíndromo se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo: Ana, Anita lava la tina
def es_palindromo(cadena):
   
    cadena = cadena.replace(" ", "").lower()
    
    
    return cadena == cadena[::-1]


palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')