# Operadores Logicos Ejemplos:
print("============================")
print("Operadores Logicos en Python")
print("============================\n")

num1 = int(input("Ingrese 1er numero: "))
num2 = int(input("Ingrese 2do numero: "))

if num1 == 5 and num2 >= 5:
    print("'And': Ambas condicionales se cumplieron")
else:
    print("'And': Una o Ambas condiones logicas no se han cumplido")

if num1 == 6 or num2 >= 8:
    print("'Or': Una o Ambas condiciones logicas se han cumplido")
else:
    print("'Or': Ambas condiciones logicas no se han cumplido")

if not num2 > 5:
    print("'Not': La condicion se invirtio y se cumple al ser menor o igual a 5")
else:
    print("'Not': La condicion no se cumple porque el numero es mayor a 5")
