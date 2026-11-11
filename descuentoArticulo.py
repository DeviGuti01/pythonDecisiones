precio = float(input("Ingrese el precio del artículo: "))

if precio > 150000:
    descuento = precio * 0.05
else:
    descuento = 0

print("El valor del descuento es: $", descuento)
