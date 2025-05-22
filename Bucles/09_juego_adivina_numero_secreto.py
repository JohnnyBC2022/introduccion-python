from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
INTENTOS_MAXIMOS = 5
adivinanza = None

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Acierta el número secreto entre 1 y 50: '))
    intentos += 1
    # Añadimos pistas para que el jugador sepa si el número proporcionado es mayor o menor que el número secreto
    if adivinanza < numero_secreto:
        print('El número secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor')

if adivinanza == numero_secreto:
    print(f'Enhorabuena, acertasete el número secreto en {intentos} intentos')
else:
    print(f'Vaya, has agotado los {INTENTOS_MAXIMOS} intentos máximos')
    print(f'El número secreto era: {numero_secreto}')
