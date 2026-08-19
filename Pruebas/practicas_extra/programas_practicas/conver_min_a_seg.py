print("==Convertidor==")
print()

seg = int(input("Ingrese cuantos segundos quiere convertir a minutos: "))
min = seg // 60
seg = seg % 60
seg = str(seg)
min = str(min)

print(f"EL resultado fue de: {min} minutos y {seg} segundos")
