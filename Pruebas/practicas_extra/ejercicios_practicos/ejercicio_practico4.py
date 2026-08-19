print("Calculadora con una sola variable\n")

print("********************")
print("* Menu de Opciones *")
print("********************\n")
print("""1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division Entera
6. Exponente
7. Modulo\n""")

num = input("Introduzca opcion deseada (1/7):")

# Suma
if num == "1":
    num = int(input("Ingrese 1er numero:"))
    num += int(input("Ingrese 2do numero:"))

    print(f"El resultado de la suma es: {num}")

# Resta
elif num == "2":
    num = int(input("Ingrese 1er numero:"))
    num -= int(input("Ingrese 2do numero:"))

    print(f"El resultado de la resta es: {num}")

# Multiplicacion
elif num == "3":
    num = int(input("Ingrese 1er numero:"))
    num *= int(input("Ingrese 2do numero:"))

    print(f"El resultado de la multiplicacion es: {num}")

# Division
elif num == "4":
    num = int(input("Ingrese 1er numero:"))
    num /= int(input("Ingrese 2do numero:"))

    print(f"El resultado de la division es: {num}")

# Division Entera
elif num == "5":
    num = int(input("Ingrese 1er numero:"))
    num //= int(input("Ingrese 2do numero:"))

    print(f"El resultado de la division entera es: {num}")

# Exponente
elif num == "6":
    num = int(input("Ingrese 1er numero:"))
    num **= int(input("Ingrese 2do numero:"))

    print(f"El resultado del exponente es: {num}")

# Modulo
elif num == "7":
    num = int(input("Ingrese 1er numero:"))
    num %= int(input("Ingrese 2do numero:"))

    print(f"El modulo de la division es: {num}")

else:
    print("Esa opcion no es valida, vuelva a ejecutar el programa")

print("\nFin.")
