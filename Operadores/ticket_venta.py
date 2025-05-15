# Ticket de Venta de una compra de un supermercado
print('*** Generador Ticket de Venta ***')
precio_leche = float(input('Precio leche:'))
precio_pan = float(input('Precio pan:'))
precio_agua = float(input('Precio agua:'))
precio_fruta = float(input('Precio fruta:'))
descuento_porcentaje = int(input('Aplicar algún descuento (%)'))

# Calcular el subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_agua + precio_fruta

# Aplicar descuento
descuento = subtotal * (descuento_porcentaje / 100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calcular el impuesto (21%)
impuesto = subtotal_con_descuento * .21

# Calculo total de la compra (incluyendo impuestos)
costo_total_compra = subtotal_con_descuento + impuesto

# Generar el ticket de venta
print(f'''
--- Ticket ---
Subtotal: {subtotal:.2f} €
Descuento: {descuento}€ ({descuento_porcentaje}%)
Subtotal con descuento: {subtotal_con_descuento:.2f}
Impuesto (21%): {impuesto:.2f} €
Total Compra: {costo_total_compra:.2f} €
''')
