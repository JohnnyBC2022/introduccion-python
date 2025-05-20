print('*** Sistema de Autentificación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '1234'

usuario = input('Introduce tu nombre de usuario: ')
password = input('Introduce tu contraseña: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print(f'Bienvenido, {usuario}')
elif usuario == USUARIO_VALIDO:
    print(f'Contraseña incorrecta')
elif password == PASSWORD_VALIDO:
    print(f'Usuario no encontrado')
else:
    print('Usuario y contraseña no encontrados')
