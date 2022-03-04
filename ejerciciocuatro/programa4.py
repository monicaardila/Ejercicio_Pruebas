'''Realice en Python una función que reciba 3 edades en el orden Juan, Mario y Pedro, luego retorne los
 mensajes expuestos.'''''

import random
from logica import contemporaneos

veces=random.randint(1,2)
print("Pruebas a realizar",veces)
for i in range(0,veces):
        Juan = random.randint(14, 15)
        Mario = random.randint(14, 15)
        Pedro = random.randint(14, 15)
        print("Edad de juan es ",Juan," y la edad de mario es ", Mario," y  edad de pedro es ", Pedro)
        contemporaneos(Juan, Mario, Pedro)