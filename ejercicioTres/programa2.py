'''Un supermercado ha puesto en oferta la venta al por mayor de cierto
producto, ofreciendo un descuento del 15% por la compra de más de
3 docenas y 10% en caso contrario. Además, por la compra de más
de 3 docenas se obsequia una unidad del producto por cada docena
en exceso sobre 3. Diseñe una función que retorne el monto de la
compra, el monto del descuento, el monto a pagar y el número de
unidades de obsequio por la compra de cierta cantidad de docenas
del producto.'''
def descuento(cantidad,obsequio):
    valor = int(input("Ingrese valor: "))

    if cantidad > 3:
        descuento = valor * 0.15
        monto = valor - descuento
        print("Las docenas llevadas son: ", cantidad)
        print("El monto a pagar es: ", monto)
        print("El monto del descuento es: ", descuento)
        print("El número de unidades de obsequio es: ", obsequio)

    else:
        descuento = valor * 0.10
        monto = valor - descuento
        print("Las docenas llevadas son: ", cantidad)
        print("El monto a pagar es: ", monto)
        print("El monto del descuento es: ", descuento)
        print("El número de unidades de obsequio es: ", 0)
