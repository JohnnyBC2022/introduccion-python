print('*** Calculadora en Python ***')
# Definimos las variables
operando1 = operando2 = resultado = 0
salir = False

while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Escoge una opción:'))
    # Solicitamos los valores
    # Validamos que no sea la opción 5
    # if opcion <= 1 and opcion <= 4:
    if 1 <= opcion <= 4:
        operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame el valor 2: '))
    # Revisamoe el tipo de operación a realizar
    if opcion == 1:  # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es {resultado:.2f}\n')
    elif opcion == 2:  # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es {resultado:.2f}\n')
    elif opcion == 3:  # Multiplicación
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es {resultado:.2f}\n')
    elif opcion == 4:  # División
        while operando2 == 0:
            print(f'No se puede dividir entre 0')
            operando2 = float(input('Dame el valor 2: '))
        if not operando2 == 0:
            resultado = operando1 / operando2
            print(f'El resultado de la división es {resultado:.2f}\n')
    elif opcion == 5:  # Salir
        print(f'Saliendo del programa...')
        salir = True
    else:
        print(f'Valor no válido. Escribe una opción correcta')
