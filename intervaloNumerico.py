x = int(input("Ingrese el numero entero x: "))

minimoValor = int(input("Ingrese el valor minimo: "))

maximoValor = int(input("Ingrese el valor maximo: "))

if minimoValor > maximoValor:
    print("Error: el minimo no puede ser mayor que el maximo")

else:
    if x >= minimoValor and x <= maximoValor:
        print("El numero esta DENTRO del intervalo")

    else:
        print("El numero esta FUERA del intervalo")
