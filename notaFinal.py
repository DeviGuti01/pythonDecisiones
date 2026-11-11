nota1 = float(input("Ingrese la nota del trabajo 1: "))

nota2 = float(input("Ingrese la nota del trabajo 2: "))

nota3 = float(input("Ingrese la nota del trabajo 3: "))

nota4 = float(input("Ingrese la nota del trabajo 4: "))

nota5 = float(input("Ingrese la nota del trabajo 5: "))

definitiva = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("La nota definitiva es:", definitiva)

if definitiva > 3.5:
    print("El estudiante GANO el curso")

else:
    print("El estudiante PERDIO el curso")
