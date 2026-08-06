"""Enunciado: Desarrollar un programa que solicite tres numero
    enteros desde teclado al usuario, posteriormente, el programa
    debera determinar e indicar a traves de un mensaje en pantalla,
    cual de los tres numeros es el mas grande.

    Requerimientos indispensables:
     EL mensaje en pantalla debera mostrar el numero
     que resulto ser el mas grande de los tres, por ejemplo:

         - "El numero 10 es el mas grande de los tres"
"""

print("=================================")
print("= Cual es el numero mas grande? =")
print("=================================\n")

num = int(input("Ingrese el 1er numero: "))
num2 = int(input("Ingrese el 2do numero: "))
num3 = int(input("Ingrese el 3er numero: "))

if num > num2 and num > num3:
    print(f"El numero {num} es el mas grande")
elif num2 > num and num2 > num3:
    print(f"EL numero {num2} es el mas grande")
elif num3 > num and num3 > num2:
    print(f"El numero {num3} es el mas grande")
else:
    print("Los tres numeros son iguales")

print("\nFin.")
