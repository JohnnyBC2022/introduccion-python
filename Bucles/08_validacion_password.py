print('*** Generación y Validación de un Password ***')

password = input('Introduce un password (debe tener al menos 6 caracteres): ')

# Validar el password
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres.')
    password = input('Introduce un nuevo valor de password: ')

print(f'El valor de password es: {password}')
