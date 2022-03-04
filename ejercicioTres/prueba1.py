'''Un supermercado ha puesto en oferta la venta al por mayor de cierto
producto, ofreciendo un descuento del 15% por la compra de más de
3 docenas y 10% en caso contrario. Además, por la compra de más
de 3 docenas se obsequia una unidad del producto por cada docena
en exceso sobre 3. Diseñe una función que retorne el monto de la
compra, el monto del descuento, el monto a pagar y el número de
unidades de obsequio por la compra de cierta cantidad de docenas
del producto.'''
import random
from programa2 import *
veces=random.randint(1,2)
print("Pruebas a realizar",veces)
for i in range(0,veces):
        docenas = random.randint(1, 20)
        obsequio=random.randint(1,2)
        descuento(docenas,obsequio)