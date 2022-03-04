'''En un parqueadero cobran $ 1.500 por hora o fracción. Diseñe una función que retorne cuanto debe pagar un
cliente por el estacionamiento de su vehículo, los parámetros de entrada son en formato (HH:MM, horas y luego los
minutos)'''
import random
from prueba1 import *

veces=random.randint(0,10)
print("Pruebas a realizar",veces)
for i in range(veces):
        prueba()