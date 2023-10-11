# Escriba un programa Python para invertir una cadena. Cadena de ejemplo: "1234abcd" Resultado esperado: "dcba4321"

def invertir_cadena(cadena):
    
    cadena_invertida = cadena[::-1]
    return cadena_invertida


cadena_ejemplo = "1234abcd"
resultado = invertir_cadena(cadena_ejemplo)
print("Resultado esperado:", resultado)

