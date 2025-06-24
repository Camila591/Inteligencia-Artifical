cantidad = int(input("ingrese la cantidad inicial de zapatos: "))
while cantidad != 0:
    Venta = int(input("¿Cuantos pares de zapatos se vendieron?: "))
    if cantidad >= Venta: 
        cantidad = cantidad  - Venta
        print("La cantidad disponible en inventario es : ", cantidad)
    else: print("Error, cantidad ingresada es mayor que el inventario")