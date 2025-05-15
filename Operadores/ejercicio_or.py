print('*** Sistema de Préstamo de Libros ***')

DISTANCIA_PERMITIDA = 3
tiene_carnet = input('¿Tienes carnet de estudiante (Si/No)?')
distancia_a_biblioteca_km = int(input('¿A cuántos kilómetros vives de la biblioteca?'))

se_puede_prestar = (tiene_carnet.lower() == 'si'
                    or distancia_a_biblioteca_km <= DISTANCIA_PERMITIDA)

print(f'¿Se puede prestar libro? {se_puede_prestar}')
