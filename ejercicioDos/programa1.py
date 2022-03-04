'''Diseñe una función que recibe un numero entero y determine si el número es o no es, par, además si es positivo o
negativo'''

def funcion(numero):
    if (numero % 2 == 0):
        print("El numero es par :",numero)
    else:
        print("El numero es impar :",numero)

def signo(numero):
    if (numero > 0):
        print("El numero es positivo :",numero)
    else:
        print("El numero es negativo :",numero)