#Objetivo: Practicar la prioridad de operaciones (uso de paréntesis) y porcentajes.
#Enunciado: Vas a comprar una laptop que cuesta $1,200.
#La tienda ofrece un 20% de descuento.
#Al precio con descuento se le aplica un 16% de impuesto (IVA).
#Calcula primero el precio tras el descuento y luego el precio final con el impuesto incluido.

laptop = 1200
descuento = laptop * 0.20
laptop = laptop - descuento
impuesto = laptop * 0.16
laptop = laptop + impuesto
print(laptop)
