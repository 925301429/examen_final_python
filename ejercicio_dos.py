"""
crear una funcion que haciendo uso del metodo filter me filtre los numeros primos de una lista pasada por parametros
"""
def filtrar_primos(numeros):
  """
  Filtra los números primos de una lista utilizando el método filter.

  Args:
    numeros: Una lista de números.

  Returns:
    Una lista con los números primos de la lista original.
  """
  def es_primo(numero):
    """
    Verifica si un número es primo.

    Args:
      numero: El número a verificar.

    Returns:
      True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
      return False
    for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0:
        return False
    return True

  primos = filter(es_primo, numeros)
  return list(primos)

# Ejemplo de uso
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
primos = filtrar_primos(numeros)
print(primos)