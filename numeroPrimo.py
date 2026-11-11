numero = int(input("Ingrese un número entero entre 0 y 20: "))

if numero < 0 or numero > 20:
    print("Número fuera del rango permitido")

else:
    if numero == 2 or numero == 3 or numero == 5 or numero == 7 or numero == 11 or numero == 13 or numero == 17 or numero == 19:
        print("El número SI es primo")

    else:
        print("El número NO es primo")
