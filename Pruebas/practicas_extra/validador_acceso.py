"""Un sistema para verificar si una persona puede entrar a un evento
    nocturno con restricción de edad y lista de invitados.
"""

edad = 19
tieneEntrada = True
listaVIP = False

if edad >= 18:
    if tieneEntrada == True:
        print("Acceso concedido al evento")
    elif listaVIP == True:
        print("Acceso VIP concedido")
    else:
        print("Acceso denegado: Se requiere entrada o pase VIP")
else:
    print("Acceso denegado: Menor de edad")

print("\nFin.")
