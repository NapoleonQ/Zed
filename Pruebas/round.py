# Prueba con Round()

"""Para poder controlar los numeros decimales que se muestran de un numero almacenado en una variable de tipo Float
    se usa round(), su estructura seria la siguiente:
        round(variable_float, el numero de decimales que deseamos mostrar)"""

# Ejemplo practico:

num = 89.78
num2 = 78.57
resul = num * num2

# Resultado sin round()
print("El resultado es: ", resul)
print()

# Resultado con round()
print("EL resultado es: ", round(resul, 2))
