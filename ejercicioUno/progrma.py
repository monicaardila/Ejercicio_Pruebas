'''En un parqueadero cobran $ 1.500 por hora o fracción. Diseñe una función que retorne cuanto debe pagar un
cliente por el estacionamiento de su vehículo, los parámetros de entrada son en formato (HH:MM, horas y luego los
minutos)'''

def cobro (tiempo):
    tiempo=tiempo.split(":")
    return (int(tiempo[0])*1500+1500)