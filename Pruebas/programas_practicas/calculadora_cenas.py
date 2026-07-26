# Enunciado: Un grupo de amigos va a cenar. Escribe un programa que calcule cuánto debe pagar cada persona.
#Define el costo total de la comida (por ejemplo, $85.00).
#Añade un 15% de propina sobre el costo total.
#Divide el total final (comida + propina) entre 4 personas.
#Resultado esperado: El costo por persona.

print("==Calculador de Cena==")
print()
costo_total = float(input("Ingrese el costo total de la Cena: "))
personas = float(input("Ingrese cuantas personas cenaron: "))
propina = costo_total * 0.15
costo_total = costo_total + propina
resul = costo_total // personas
print()
print("==Nota: Se le anadira un 15% de propina para los Mesoneros==")
print()
print("El costo total por persona es de: " + str(resul))
