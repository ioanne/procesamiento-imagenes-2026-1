"""
DOCString pepe
"""

# variables
numero = 10 # entero
precio = 10.5 # flotante
texto = "Hola mundo" # cadena texto
verdadero = True # boolean
falso = False # boolean
vacio = None # valor nulo (ausencia de)

lista = [1, 2, 3, 4, 5] # lista
diccionario = { 'clave1': 'valor1', 'clave2': 'valor2' } # diccionario
tupla = 1, 2, 3 # tupla
coleccion = {1, 2, 3} # colección (set)

"""
Reglas de los conjuntos:
No se puede repetir valores
No se puede poner valores mutables (listas, diccionarios, tuplas)
Son desordenados (no tienen un orden específico)
Al convertir una lista a un conjunto, se eliminan los valores repetidos
Al convertir un conjunto a una lista, se pierde el orden de los elementos
"""

"""
Slice de listas:
lista[start:stop:step]
start: índice de inicio (inclusive)
stop: índice de fin (exclusive)
step: paso (opcional, por defecto es 1)
"""

"""
Tuplas:
Son inmutables (no se pueden modificar después de su creación)
"""

"""
Las listas son mutables (se pueden modificar después de su creación)

lista = [1, 2, 3, 4, 5] # lista
lista2 = lista # lista2 apunta a la misma lista que lista
lista.append(6) # se modifica la lista original
print(lista) # [1, 2, 3, 4, 5, 6]
print(lista2) # [1, 2, 3, 4, 5, 6]

Podemos hacer una copia no profunda
lista3 = lista.copy() # lista3 es una copia de lista
lista.append(7) # se modifica la lista original
print(lista) # [1, 2, 3, 4, 5, 6, 7]
print(lista3) # [1, 2, 3, 4, 5, 6]

Copia profunda
import copy
lista = [1, 2, 3, 4, [1, 2, 3]] # lista original
lista4 = copy.deepcopy(lista) # lista4 es una copia profunda de lista
La copia profunda crea una lista completamente independiente de la original, incluyendo las sublistas.
Por lo tanto, cualquier modificación en la lista original no afectará a la copia profunda.

"""

# Comentario de una linea
# type hint
# Declaración de la función
def foo(arg1: int, arg2: str) -> int: # Firma
    """
    DOCString de la funcion foo
    :param arg1: descripcion del argumento 1
    :param arg2: descripcion del argumento 2
    """
    # Comentario de la funcion foo
    return 10 # resultado hardcodeado

# Uso de una función
resultado = foo(5, "hola")
