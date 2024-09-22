# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
# Primera llamada a la función (utilizando el valor predeterminado del porcentaje de descuento)
monto_total1 = 500  # Monto total de la primera compra
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1
print(f"Compra 1:\nMonto Total: ${monto_total1}\nDescuento Aplicado (10%): ${descuento1}\nMonto Final: ${monto_final1}\n")

# Segunda llamada a la función (especificando un porcentaje de descuento diferente)
monto_total2 = 750  # Monto total de la segunda compra
porcentaje_descuento2 = 15  # Porcentaje de descuento especificado
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print(f"Compra 2:\nMonto Total: ${monto_total2}\nDescuento Aplicado ({porcentaje_descuento2}%): ${descuento2}\nMonto Final: ${monto_final2}")
