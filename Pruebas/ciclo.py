opcion = 'y'

while opcion != 'n':
    print("Bienvenido a esta sumatoria\n")
    num = float(input("Ingrese primer numero: "))
    num2 = float(input("Ingrese segundo numero: "))
    resul = num + num2

    # Ciclo para repetir la pregunta hasta que una opcion valida
    while True:
        print(f"\nEl resultado de la sumaria es: {resul}")
        opcion = input("Quiere repetir sumatoria? (Y/N): ").lower()

        # Or en vez de And
        if opcion == 'y' or opcion == 'n':
            break
        else:
            print("Opcion Invalida, intente de nuevo")

print("\nFin.")
