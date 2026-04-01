# 

tupla = (1,2,3)

a,b,c = (1,2,3)

print(a)
print(b)
print(c)


def foo(a,b,c) -> tuple:
    return a,b,c

a,b,c = foo(1,2,3)

def process_image(image) -> tuple:
    # proceso la imagen
    a,b,c = None, None, None # variables auxiliares
    new_image = image # nueva imagen procesada
    has_changes = True # variable que indica si la imagen ha cambiado
    return has_changes, new_image

has_changes, new_image = process_image('imagen.jpg')

a = b = c = None # No tan usado

a = None;b = None;c = None # Menos usado

# mas usado
a = 1
b = 1
c = 1

a,b,c = None, None, None # mas usado para asignar valores a varias variables al mismo tiempo

diccionario = {
    'lista_de_cosas': [[[[[]]]]],
    'diccionario_de_cosas': {
        'clave1': {
            'clave2': {
                'clave3': [1,2,{1,2,3}, (1,2,3), {'clave4': 'valor4'}]
            }
        }
    },
}

diccionario = {
    'lista_de_cosas': [[[[[]]]]],
    'diccionario_de_cosas': {
        'clave1': None
    },
}

dict2 = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': {
        'clave4': 'valor4',
        'clave5': 'valor5',
        'clave6': {
            'clave7': 'valor7',
            'clave8': 'valor8',
        },
    },
}

dict2['clave3']['clave6']
dict2['clave3']['clave6']['clave7']
dict2['clave3']['clave6']['clave8']

# JSON Javascript object notation
# DUMPS / LOADS
# import json
# json.dumps(diccionario) # convierte un diccionario a una cadena JSON
# json.loads(json_request) # convierte una cadena JSON a un diccionario
"{}"
import json

json.loads('{"clave1": "valor1", "clave2": null}') # convierte una cadena JSON a un diccionario

resultado = diccionario['diccionario_de_cosas']['clave1']['clave2']['clave3'] # Esto
resultado = diccionario.get('diccionario_de_cosas', {}).get('clave1', {}).get('clave2', {}).get('clave3')

if resultado is not None:
    pass
    # hago algo.
else:
    pass
    # armo una respuesta con diccionario, para ver que vino mal
    # y lo loggeo
hola = "hola i'm a string"
hola = 'hola i\'m a string' # escape de comillas simples


# Para las clases se usa upper camel case.
class Vehiculo:
    def __init__(self, color):
        self.color = color
        self.acelerando = False
        print(self)
    
    def acelerar(self, intensidad):
        # algoritmo
        self.acelerando = True
        print(f"Acelerando")

vehiculo = Vehiculo(color="Rojo") # instanciar la clase vehiculo
print(vehiculo.acelerando)
print(vehiculo)
vehiculo.acelerar(intensidad=10)
print(vehiculo.acelerando)


# Herencia (Es un pilar de POO)
class Auto(Vehiculo):
    pass

