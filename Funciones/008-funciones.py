# Escriba una función de Python que acepte una cadena y calcule el número de letras mayúsculas y minúsculas
def contar_letras_mayusculas_y_minusculas(cadena):
    
    mayusculas = 0
    minusculas = 0

  
    for caracter in cadena:
       
        if caracter.isupper():
            mayusculas += 1
      
        elif caracter.islower():
            minusculas += 1

    
    return mayusculas, minusculas


cadena = "Hola Mundo 123"
mayusculas, minusculas = contar_letras_mayusculas_y_minusculas(cadena)
print("Letras mayúsculas:", mayusculas)
print("Letras minúsculas:", minusculas)