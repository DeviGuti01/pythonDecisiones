litros = float(input("Ingrese la cantidad de litros del tanque: "))

if litros < 250:
    print("La llave debe estar ABIERTA")

elif litros > 450:
    print("La llave debe estar CERRADA")

else:
    print("La cantidad de agua está en el rango permitido")