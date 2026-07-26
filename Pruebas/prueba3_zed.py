# Prueba con Strings en Zed 3
# Prueba 3: Busqueda

mensj = "Buenas tardes, Bienvenido a este Programa Senor/a"
mensj += " "
user = input("Ingrese nombre de usuario: ")
mensj += user
busq_user = mensj.find(user)
auten = busq_user + 3
auten = str(auten)

print(mensj)
print("Numero de posicion en la cadena de caracteres: " + auten)
