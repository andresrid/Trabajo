# Escriba una función de Python que tome una lista y devuelva una nueva lista con elementos únicos de la primera lista
def elementos_unicos(lista):
    
    lista_unicos = list(set(lista))
    return lista_unicos


mi_lista = [1, 2, 2, 3, 4, 4, 5]
resultado = elementos_unicos(mi_lista)
print(resultado)