'''En un parqueadero cobran $ 1.500 por hora o fracción. Diseñe una función que retorne cuanto debe pagar un
cliente por el estacionamiento de su vehículo, los parámetros de entrada son en formato (HH:MM, horas y luego los
minutos)'''
import random
from progrma import *
def prueba():

    hora=random.randint(0,23)
    minuto=random.randint(0,59)
    llega=cobro(str(hora) + ":"+ str(minuto))
    print("horas: ",hora,"minutos: ",minuto,"=",llega)