"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""
tiendas = {
    1: {"nombre": "Librería El Lector", "horario": "Lunes a Viernes 9:00-7:00"},
    2: {"nombre": "Cafetería La Esquina", "horario": "Lunes a Domingo 8:00-8:00"},
    3: {"nombre": "Supermercado El Barato", "horario": "Lunes a Sábado 7:00-7:00"},
    4: {"nombre": "Farmacia Salud", "horario": "Lunes a Domingo 24 horas"},
    5: {"nombre": "Zapatería La Moda", "horario": "Lunes a Viernes 10:00-8:00"}
}

def editar_nombre(id_tienda, nuevo_nombre):
    """
    Edita el nombre de una tienda comercial.

    Args:
        id_tienda: El ID de la tienda a editar.
        nuevo_nombre: El nuevo nombre de la tienda.
    """
    if id_tienda in tiendas:
        tiendas[id_tienda]["nombre"] = nuevo_nombre
        print(f"El nombre de la tienda {id_tienda} se ha actualizado a {nuevo_nombre}.")
    else:
        print(f"No se encontró la tienda con ID {id_tienda}.")

def actualizar_horario(id_tienda, nuevo_horario):
    """
    Actualiza el horario de atención de una tienda comercial.

    Args:
        id_tienda: El ID de la tienda a actualizar.
        nuevo_horario: El nuevo horario de atención.
    """
    if id_tienda in tiendas:
        tiendas[id_tienda]["horario"] = nuevo_horario
        print(f"El horario de la tienda {id_tienda} se ha actualizado a {nuevo_horario}.")
    else:
        print(f"No se encontró la tienda con ID {id_tienda}.")

def eliminar_tienda(id_tienda):
    """
    Elimina una tienda comercial del diccionario.

    Args:
        id_tienda: El ID de la tienda a eliminar.
    """
    if id_tienda in tiendas:
        del tiendas[id_tienda]
        print(f"La tienda {id_tienda} se ha eliminado.")
    else:
        print(f"No se encontró la tienda con ID {id_tienda}.")

# Ejemplo de uso
editar_nombre(1, "Librería El Libro")
actualizar_horario(2, "Lunes a Domingo 9:00-8:00")
eliminar_tienda(3)
print(tiendas)