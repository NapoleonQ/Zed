# Ejercicio Practico para comprenderlo:
print("=========")
print("Conversor")
print("========= \n")

print("Menu de Opciones: \n")
print("Ingrese 1 para ir al conversor de numeros a palabras")
print("Ingrese 2 para ir al conversor de palabras a numeros \n")

opcion = int(input("Cual es su opcion (1/2): "))
print()

if opcion == 1:
    print("===============================")
    print("Conversor de numeros a palabras")
    print("=============================== \n")

    num = int(input("Ingrese el numero a convertir: "))

    if num == 1:
        print("El numero es 'Uno'")
    elif num == 2:
        print("El numero es 'Dos'")
    elif num == 3:
        print("El numero es 'Tres'")
    elif num == 4:
        print("El numero es 'Cuatro'")
    elif num == 5:
        print("El numero es 'Cinco'")
    else:
        print("El programa solo puede convertir hasta 5")
elif opcion == 2:
    print("===============================")
    print("Conversor de palabras a numeros")
    print("=============================== \n")

    num = input("Ingrese el palabra a convertir: ")
    num = num.lower()

    if num == "uno":
        print("El numero es '1'")
    elif num == "dos":
        print("El numero es '2'")
    elif num == "tres":
        print("El numero es '3'")
    elif num == "cuatro":
        print("El numero es '4'")
    elif num == "cinco":
        print("El numero es '5'")
    else:
        print("Valor Invalido")
else:
    print("Numero de Opcion invalido")

print("\n Fin.")
