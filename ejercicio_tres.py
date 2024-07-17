"""
crear un funcion que me retorne un diccioonario de la cantidad de vocales que aparecen
 en un texto pasado por parametro el diccionario debera ser 
 credo por comprension de diccionarios
ejm:
entrada: eucalipto
salida: {e:1,u:1,a:1,i:1,o:1}
"""
def contar_vocales(texto):
  """
  Función que cuenta la cantidad de vocales en un texto y devuelve un diccionario con las vocales como claves y su conteo como valores.

  Args:
    texto: El texto a analizar.

  Returns:
    Un diccionario con las vocales como claves y su conteo como valores.
  """
  vocales = 'aeiou'
  conteo_vocales = {vocal: texto.count(vocal) for vocal in vocales}
  return conteo_vocales

# Ejemplo de uso
texto = "eucalipto"
resultado = contar_vocales(texto)
print(resultado)