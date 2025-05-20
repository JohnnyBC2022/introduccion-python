print('*** El mayor de dos números ***')

numero1 = int(input('Escribe el número 1: '))
numero2 = int(input('Escribe el número 2: '))

# El mayor de dos números
if numero1 > numero2:
    print(f'El número {numero1} es mayor')
else:
    print(f'El número {numero2} es mayor')

# Sintaxis alternativa con operador ternario (cambia respecto a Javascript)
# Javascript: condicion ? codigo_true : codigo_false
# Python: codigo_true if condicion else codigo_false

print(f'El número {numero1} es mayor') if numero1 > numero2 else print(f'El número {numero2} es mayor')
