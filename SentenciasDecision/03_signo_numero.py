print('*** Revisa el signo de un número ***')
numero = int(input('Escribe un número:'))

if numero > 0:
    print(f'El número {numero} es positivo')
elif numero < 0:
    print(f'El número {numero} es negativo')
else:
    print(f'El número {numero} es cero')
