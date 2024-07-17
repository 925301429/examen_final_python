"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def crear_diccionario_alumno(nombre, apellido, edad, programa_estudio, semestre):
  """
  Crea un diccionario con los datos personales de un alumno.

  Args:
    nombre: El nombre del alumno.
    apellido: El apellido del alumno.
    edad: La edad del alumno.
    programa_estudio: El programa de estudio del alumno.
    semestre: El semestre en el que está el alumno.

  Returns:
    Un diccionario con los datos personales del alumno.
  """
  alumno = {
      "nombre": nombre,
      "apellido": apellido,
      "edad": edad,
      "programa_estudio": programa_estudio,
      "semestre": semestre
  }
  return alumno

# Ejemplo de uso
datos_alumno = ("jose", "alvarez", "30", "APSTI", "III")
diccionario_alumno = crear_diccionario_alumno(*datos_alumno)
print(diccionario_alumno)