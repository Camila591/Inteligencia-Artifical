"""
compras = []
i = 0
while i < 5:
    articulo = int(input("ingrese el valor del articulo: "))
    compras.append(articulo)
    i + = 1
print(f"El precio de los articulos que usted compro son: {compras}")
print(f"El articulo mas caro que usted compro es: {max(compras)}")
"""
compra =[]
producto = 0
perro = 0
hamburguesa = 0
pizza = 0
salchipapa = 0
print("Restaurante Trique Traque\n1.PERRO CALIENTE = 10000\n2.HAMBUERGUESA = 18000\n3.PIZZA = 11000\n4.SALCHIPAPA = 12000\n5.TERMINAR")
while producto != 5:
    producto = int(input("Ingrese la numeración del producto que desea adquirir: "))
    if producto == 1:
        compra.append(10000)
        perro += 1
    elif producto == 2:
        compra.append(18000)
        hamburguesa += 1
    elif producto == 3:
        compra.append(11000)
        pizza += 1
    elif producto == 4:
        compra.append(12000)
        salchipapa += 1
    else:
        print(f"Los precios de los articulos son: {compra}")
        print(f"El valor total de los productos es: {sum(compra)}")
        print(f"El total de perros es de: {perro} por valor de {perro*10000}")
        print(f"El total de hamburguesas es de: {hamburguesa} por valor de {hamburguesa*18000}")
        print(f"El total de pizza es de: {pizza} por valor de {pizza*11000}")
        print(f"El total de salchipapa es de: {salchipapa} por valor de {salchipapa*12000}")