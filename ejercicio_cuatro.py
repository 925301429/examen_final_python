"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
alumno = {
    "nombre": "Juan Pérez",
    "edad": 18,
    "carrera": "Ingeniería en Sistemas"
}

def imprimir_registro():
    """Imprime los registros del alumno."""
    print("Nombre:", alumno["nombre"])
    print("Edad:", alumno["edad"])
    print("Carrera:", alumno["carrera"])

def editar_campo(campo, nuevo_valor):
    """Edita un campo del registro del alumno.

    Args:
        campo: El nombre del campo a editar.
        nuevo_valor: El nuevo valor del campo.
    """
    if campo in alumno:
        alumno[campo] = nuevo_valor
        print(f"El campo '{campo}' se ha actualizado a '{nuevo_valor}'.")
    else:
        print(f"El campo '{campo}' no existe en el registro.")

# Ejemplo de uso
imprimir_registro()

editar_campo("edad", 19)
imprimir_registro()