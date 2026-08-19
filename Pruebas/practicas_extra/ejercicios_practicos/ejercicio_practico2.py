"""Enunciado: Desarrolar un programa que solicite un numero
    entero desde el teclado al usuario. posteriormente,
     el programa debera determinar e indicar a traves de un mensaje,
     si el numero introducido es par o impar

     Requerimientos indispensables:
         El mensaje en pantalla debera mostrar la frase: 'el numero es par o impar',
          junto con el numero que el usuario introdujo desde el teclado,
          por ejemplo:
              "El numero 8 es par"
              "El numero 5 es impar"

"""

print("=======================")
print("= Numero par o Impar? =")
print("=======================\n")

num = int(input("Ingrese su numero: "))

if (num % 2) == 0:
    print("=======================")
    print("= Numero par o Impar? =")
    print("=======================\n")

    print(f"El numero {num} es par")
else:
    print("=======================")
    print("= Numero par o Impar? =")
    print("=======================\n")

    print(f"El numero {num} es impar")

print("\nFin.")
