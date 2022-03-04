'''Realice en Python una función que reciba 3 edades en el orden Juan, Mario y Pedro, luego retorne los
 mensajes expuestos.'''

def contemporaneos(Juan, Mario, Pedro):
    if (Juan == Mario) and (Mario == Pedro):
        print("Los tres son contemporaneos")
    elif (Juan == Mario):
        print("Juan  y Mario  son contemporaneos")
    elif (Juan == Pedro):
        print("Juan y Pedro son contemporaneos")
    elif (Mario == Pedro):
        print("Mario y Pedro son contemporaneos")
    else:
        print("No hay contemporaneos")
