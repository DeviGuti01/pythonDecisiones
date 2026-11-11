x = int(input("Ingrese el número entero x: "))

min1 = int(input("Ingrese el mínimo del intervalo 1: "))
max1 = int(input("Ingrese el máximo del intervalo 1: "))

min2 = int(input("Ingrese el mínimo del intervalo 2: "))
max2 = int(input("Ingrese el máximo del intervalo 2: "))

min3 = int(input("Ingrese el mínimo del intervalo 3: "))
max3 = int(input("Ingrese el máximo del intervalo 3: "))

if (x > min1 and x < max1) or (x > min2 and x < max2) or (x > min3 and x < max3):
    print("El número está DENTRO de uno de los intervalos")

else:
    print("El número está FUERA de los tres intervalos")
