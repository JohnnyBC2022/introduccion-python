print('*** Sistema de Administrador de Cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Selecciona una opción: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema...\n')
        salir = True
    else:
        print('Opción no válida.\n')
