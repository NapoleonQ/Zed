# Operadores Relacionales;

print("Introduce dos numeros a comparar: \n")

num1 = int(input("Introduzca su 1er numero: "))
num2 = int(input("Introduzca su 2do numero: "))

print(f"\n Numeros a comparar: {num1} y {num2}\n")

if num1 == num2:
    print("Es igual que...")
if num1 != num2:
    print("Es diferente...")
if num1 > num2:
    print("Es mayor...")
if num1 < num2:
    print("Es menor...")
if num1 >= num2:
    print("Es mayor o igual...")
if num1 <= num2:
    print("Es menor o igual...")
else:
    print("Valor invalido")

print("\nFin.")
