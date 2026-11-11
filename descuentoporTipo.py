precio = float(input("Ingrese el precio del artículo: "))

print("Seleccione el tipo de artículo:")
print("1. Textil")
print("2. Electrodoméstico")
print("3. Elementos de cocina")
print("4. Video juego")

tipo = int(input("Digite el tipo de artículo: "))

if tipo == 1:
    porcentaje = 0

elif tipo == 2:
    porcentaje = 3.7

elif tipo == 3:
    porcentaje = 4.2

elif tipo == 4:
    porcentaje = 7.8

else:
    porcentaje = -1

if porcentaje == -1:
    print("Tipo de artículo no válido")

else:
    descuento = precio * porcentaje / 100

    print("El porcentaje de descuento es:", porcentaje, "%")
    print("El valor del descuento es: $", descuento)
