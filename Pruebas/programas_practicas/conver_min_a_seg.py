#Objetivo: Practicar la división entera (//) y el residuo o módulo (%).
#Enunciado: Un video dura 845 segundos. Escribe un programa que convierta ese tiempo a minutos y segundos restantes.
#Usa la división entera (//) para obtener la cantidad total de minutos completos.
#Usa el operador módulo (%) para obtener los segundos que sobran.
#Resultado esperado: Los minutos enteros y los segundos restantes (por ejemplo: 14 minutos y 5 segundos).

print("==Convertidor==")
print()

seg = int(input("Ingrese cuantos segundos quiere convertir a minutos: "))
min = seg // 60
seg = seg % 60
seg = str(seg)
min = str(min)

print("EL resultado fue de: " + min + " minutos y " + seg + " segundos")
