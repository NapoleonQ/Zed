# Prueba con Strigs en Zed 4
# Sumatorio con Ciclos

print("== Sumatoria ==")
print()

num_uno = float(input("Ingrese un numero: "))
num_dos = float(input("Ingrese otro numero: "))
resul_sum = num_uno + num_dos
resul_sum = str(resul_sum)
print()
print("El resultado de la sumatoria es: " + resul_sum)
opcion = input("Quieres volver a sumar? (1/2): ")

while opcion == "1":
    print()
    num_uno = float(input("Ingrese un numero: "))
    num_dos = float(input("Ingrese otro numero: "))
    resul_sum = num_uno + num_dos
    resul_sum = str(resul_sum)
    print()
    print("El resultado de la sumatoria es: " + resul_sum)
    opcion = input("Quieres volver a sumar? (1/2): ")
# else:
    # print()
    # print("Fin de la Sumatoria")
