"""
crear un funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_minimo_maximo(lista):
    minimo = min(lista)
    maximo = max(lista)
    return {'menor': minimo, 'mayor': maximo}

# Ejemplo de uso
entrada = [4, 7, 10, 4, 1, 0]
resultado = encontrar_minimo_maximo(entrada)
print(resultado)