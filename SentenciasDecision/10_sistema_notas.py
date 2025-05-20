print('*** Sistema de Notas ***')

nota = float(input('Introduce una nota entre 0 y 10: '))
nota_letra = ''
# Revisamos si esta dentro de los rangos
if nota >= 9 and nota <= 10:
    nota_letra = 'Sobresaliente'
elif nota >= 7 and nota < 9:
    nota_letra = 'Notable'
elif nota >= 6 and nota < 7:
    nota_letra = 'Bien'
elif nota >= 5 and nota < 6:
    nota_letra = 'Aprobado'
elif nota >= 0 and nota < 5:
    nota_letra = 'Suspenso'
else:
    nota_letra = 'Introduce un valor válido'

print(f'La nota {nota} equivale a: {nota_letra}')

# Sintaxis abreviada:
if 9 <= nota <= 10:
    nota_letra = 'Sobresaliente'
elif 7 <= nota < 9:
    nota_letra = 'Notable'
elif 6 <= nota < 7:
    nota_letra = 'Bien'
elif 5 <= nota < 6:
    nota_letra = 'Aprobado'
elif 0 <= nota < 5:
    nota_letra = 'Suspenso'
else:
    nota_letra = 'Introduce un valor válido'

# Imprimimos el resultado
print(f'La nota {nota} equivale a: {nota_letra}')
