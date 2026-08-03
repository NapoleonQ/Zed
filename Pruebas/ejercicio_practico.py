"""Enunciado: La compania multinacional 'Rappi', solicita un sistema que determine los dias de vacaciones a los que tiene derecho un trabajador,
    tomando en cuenta las siguientes caracteristicas:

    Existen tres departamentos dentro de la compania con sus respectivas claves:
    1: Departamento de Atencion al cliente (Clave 1)
    2: Departamento de Logistica (Clave 2)
    3: Gerencia (Clave 3)

    Trabajadores con Clave 1:
        Con 1y de servicio, reciben 6 dias de vacaciones
        Con 2 a 6y de servicio, reciben 14 dias de vacaciones
        A partir de 7y de servicio, reciben 20 dias de vacaciones

    Trabajadores con Clave 2:
        Con 1y de servicio, reciben 7 dias de vacaciones
        Con 2 a 6y de servicio, reciben 15 dias de vacaciones
        A partir de 7y de servicio, reciben 22 dias de vacaciones

    Trabajadores con Clave 3:
        Con 1y de servicio, reciben 10 dias de vacaciones
        Con 2 a 6y de servicio, reciben 20 dias de vacaciones
        A partir de 7y de servicio, reciben 30 dias de vacaciones

    Requerimientos indispensables:
        El sistema debe solicitar el NOMBRE, CLAVE y ANTIGUEDAD del trabajador desde el teclado
         Posteriormente el programa debe mostrar un mensaje en pantalla, que contenga el nombre
         del trabajador y los dias de vacaciones a los que tiene derecho.

    """

# Propuesta 1:
print("===============================")
print("= Sistema de Vacaciones Rappi =")
print("===============================\n")

nombre = input("Ingrese el nombre del empleado: ")
clave = int(input("Ingrese su clave de departamento: "))
antiguedad = float(input("Ingrese su antiguedad en la empresa: "))

if clave == 1:
    if antiguedad >= 7:
        print(f"{nombre}, usted tiene 20 dias de vacaciones")
    elif antiguedad >= 2:
        print(f"{nombre}, usted tiene 14 dias de vacaciones")
    elif antiguedad >= 1:
        print(f"{nombre}, usted tiene 6 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave == 2:
    if antiguedad >= 7:
        print(f"{nombre}, usted tiene 22 dias de vacaciones")
    elif antiguedad >= 2:
        print(f"{nombre}, usted tiene 15 dias de vacaciones")
    elif antiguedad >= 1:
        print(f"{nombre}, usted tiene 7 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
elif clave == 3:
    if antiguedad >= 7:
        print(f"{nombre}, usted tiene 30 dias de vacaciones")
    elif antiguedad >= 2:
        print(f"{nombre}, usted tiene 20 dias de vacaciones")
    elif antiguedad >= 1:
        print(f"{nombre}, usted tiene 10 dias de vacaciones")
    else:
        print("Sin derecho a vacaciones")
else:
    print("La clave no existe")

print("\nFin.")
