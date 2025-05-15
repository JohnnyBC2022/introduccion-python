print('*** Sistema de Descuentos VIP ***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('¿Cuántos productos compraste hoy?'))
es_socio = input('¿Tienes tarjeta de socio? (Si/No)')

aplica_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                    and es_socio.lower() == 'si')

print(f'¿Tienes acceso al descuento VIP? {aplica_descuento}')
