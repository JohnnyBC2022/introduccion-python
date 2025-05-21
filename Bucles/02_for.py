print('*** Bucle For ***')

# Usaremos la función range: range(start,[end],[step]) pero sería >=start, <end

# Imprimir del 0 al 4
for contador in range(5):  # crea el rango de 0 a 4
    print(f'Contador: {contador}')

# Imprimir del 1 al 5
for contador2 in range(1, 6):
    print(f'Contador 2: {contador2}')

# Imprimir del 0 al 10 de 2 en 2
for contador3 in range(0, 11, 2):  # si le ponemos 12 hace lo mismo porque el último numero no lo añade al rango
    print(f'Contador 3: {contador3}')
