# Definimos la función calcular_descuento
def calcular_descuento(monto_total, porcentaje=10):
    """
    Calcula el descuento en función del monto total y el porcentaje de descuento.

    Parámetros:
    monto_total (float): El monto total sobre el que se aplicará el descuento.
    porcentaje (float, opcional): El porcentaje de descuento a aplicar. El valor predeterminado es 10%.

    Retorno:
    float: El valor del descuento redondeado a dos decimales.
    """
    # Calcula el monto del descuento
    descuento = monto_total * porcentaje / 100
    # Devuelve el descuento redondeado a dos decimales
    return round(descuento, 2)

# Ejemplo 1: Usando el porcentaje predeterminado del 10%
monto_total = 23689  # Definimos el monto total para el primer ejemplo
# Llamamos a la función calcular_descuento con el monto_total y el porcentaje predeterminado (10%)
descuento = calcular_descuento(monto_total)
# Calculamos el monto final restando el descuento al monto total
monto_final = monto_total - descuento
# Mostramos los resultados: monto total, descuento aplicado y monto final a pagar
print(f"Monto total: $ {monto_total:.2f}, Descuento: $ {descuento:.2f}, Monto a pagar: $ {monto_final:.2f}")

# Ejemplo 2: Usando un porcentaje de descuento personalizado del 40%
monto_total2 = 46822  # Definimos el monto total para el segundo ejemplo
porcentaje_descuento = 40  # Definimos el porcentaje de descuento personalizado
# Llamamos a la función calcular_descuento con el monto_total2 y el porcentaje del 40%
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento)
# Calculamos el monto final restando el descuento al monto total
monto_final2 = monto_total2 - descuento2
# Mostramos los resultados: monto total, descuento aplicado y monto final a pagar
print(f"Monto total: $ {monto_total2:.2f}, Descuento: $ {descuento2:.2f}, Monto a pagar: $ {monto_final2:.2f}")

# Ejemplo 3: Solicitar al usuario que ingrese el monto total de la compra
monto_total_usuario = float(input("Ingrese el monto total de la compra: "))  # Capturamos el monto total ingresado por el usuario
# Llamamos a la función calcular_descuento con el monto ingresado por el usuario y el porcentaje predeterminado (10%)
descuento_usuario = calcular_descuento(monto_total_usuario)
# Calculamos el monto final restando el descuento al monto total ingresado por el usuario
monto_final_usuario = monto_total_usuario - descuento_usuario
# Mostramos los resultados para el monto ingresado por el usuario
print(f"Descuento para un monto total de $ {monto_total_usuario:.2f}, Descuento: $ {descuento_usuario:.2f}, Monto a pagar: $ {monto_final_usuario:.2f}")
