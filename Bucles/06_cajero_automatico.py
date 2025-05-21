print('*** Cajero Automático ***')

saldo = 1000  # saldo inicial
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Ingresar
    4. Salir''')
    opcion = int(input('Selecciona una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: {saldo:.2f} €\n')
    elif opcion == 2:
        retirada = float(input('Introduce la cantidad a retirar: '))
        # Validación
        if retirada <= saldo:
            saldo -= retirada  # saldo = saldo - retirada
            print(f'Tu saldo actual es: {saldo:.2f} €\n')
        else:
            print(f'Saldo insuficiente, no puedes retirar. Saldo actual: {saldo:.2f} €\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        if deposito > 100000:
            print('¿Dónde vas, quién eres Amancio Ortega?\n')
        else:
            saldo += deposito  # saldo = saldo + deposito
        print(f'Tu saldo actual es: {saldo:.2f} €\n')
    elif opcion == 4:
        print('Saliendo del cajero automático. Hasta Pronto')
        salir = True
    else:
        print('Opción no válida. Introduce otra opción.')
