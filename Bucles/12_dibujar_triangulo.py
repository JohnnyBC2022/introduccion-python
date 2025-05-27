print('*** Dibujar Triángulo Simétrico ***')

numero_de_filas = int(input('Escribe el número de filas: '))
simbolo = input('Escribe un caracter o símbolo: ')

# Iterar sobre cada fila del triángulo
for fila in range(1, numero_de_filas + 1):
    espacios_en_blanco = " " * (
            numero_de_filas - fila)  # Cálculo de la cantidad de espacios en blanco que se necesitan por fila
    caracteres = simbolo * (2 * fila - 1)  # Calcular la cantidad de caracteres para la fila actual
    print(f'{espacios_en_blanco}{caracteres}')  # Imprimimos la figura
