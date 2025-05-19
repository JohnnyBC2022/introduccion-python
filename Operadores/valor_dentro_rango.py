print('*** Valor dentro de rango ***')

# Condiciones
MINIMO = 0
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input('Introduce un número entre 0 y 5:'))

# Verificamos si estamos dentro del rango
dentro_rango = dato >= MINIMO and dato <= MAXIMO

# Sintaxis alternativa
dentro_rango = MINIMO <= dato <= MAXIMO
print(f'¿Valor dentro de rango? {dentro_rango}')
