# Sistema para Calcular promedio de notas

alumno = input("Ingrese su nombre: ")
nota1 = float(input(f"{alumno}, Cual es tu calificacion en Matematicas? (0/10): "))
nota2 = float(input(f"{alumno}, Cual es tu calificacion en Fisica? (0/10): "))
nota3 = float(input(f"{alumno}, Cual es tu calificacion en Quimica? (0/10): "))
print()
promedio = (nota1 + nota2 + nota3) // 3

if promedio >= 6:
    print(f"Felicidades {alumno}, has aprobado con: {promedio}")
else:
    print(f"Lo siento {alumno}, has reprobado con: {promedio}")

print()
print("Fin.")
