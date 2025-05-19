print('*** Sistema de Descuentos ***')

# Condiciones
COMPRA_MINIMA_DESC = 1000

total_compra = float(input('¿Cuál fué el importe total de la compra?'))
es_miembro = input('¿Es socio de la tienda (si/no)?')

# Verficar los datos del cliente
if total_compra >= COMPRA_MINIMA_DESC and es_miembro.lower() == 'si':
    descuento = 0.1  # Descuento del 10%
elif es_miembro.lower() == 'si':
    descuento = .05  # Descuento del 5%
else:
    descuento = 0

# Hacemos los cálculos
if descuento != 0:
    total_descuento = total_compra * descuento
    total_final = total_compra - total_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100}%')
    print(f'Total de la compra: {total_compra}')
    print(f'Total de la compra con descuento: {total_final}')
else:
    print(f'\nNo se obtuvo ningún descuento')
    print(f'¿Quiéres hacerte socio de la tienda?')
    print(f'Total de la compra: {total_compra}')
