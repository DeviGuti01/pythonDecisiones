a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática")

else:
    discriminante = b**2 - 4*a*c

    if discriminante >= 0:
        print("La ecuación SI tiene solución real")

    else:
        print("La ecuación NO tiene solución real")