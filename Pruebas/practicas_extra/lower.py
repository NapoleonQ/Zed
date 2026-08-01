
"""Aprendi que era .lower(), es una funcion que implementada por Python para convertir
    una cadena de caracteres en minusculas, un ejemplo de como se usaria:

     cadena = Input("Ingrese valor: ")
     cadena = cadena.lower()
              Esta sentencia convierte los caracteres de la cadena en minusculas
     y las guarda nuevamente en la variable
"""

# Test siguiendo el Ejemplo:

opcion = input("Escriba 'Manzana', 'Platano' o 'Pera': ")
opcion = opcion.lower()

if opcion == "manzana":
    print("Dato curioso: Las manzanas flotan en el agua.")
elif opcion == "platano":
    print("Dato curioso: Los plátanos son técnicamente bayas.")
elif opcion == "pera":
    print("Dato curioso: Las peras son parientes cercanas de las rosas y de las manzanas.")
else:
    print("Opcion no disponible.")

print("\n Fin.")
