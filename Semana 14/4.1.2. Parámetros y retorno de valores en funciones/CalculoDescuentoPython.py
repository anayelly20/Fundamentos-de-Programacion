# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
def main():
    # Primera llamada: solo se proporciona el monto total de la compra
    monto_total_1 = 1000
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Monto total: ${monto_total_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}")
    print()

    # Segunda llamada: se proporciona tanto el monto total de la compra como el porcentaje de descuento
    monto_total_2 = 1500
    porcentaje_descuento_2 = 15
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"Monto total: ${monto_total_2}")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
