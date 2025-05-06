from generador_id_unico import apellido

print('*** Sistema Generador de Emails ***')
nombre = input('¿Cuál es tu nombre?')
# nombre_minusuculas = nombre.lower()
apellido = input('¿Cuál es tu apellido?')

# Generar el email
email_generado = f'{nombre.lower()}.{apellido.lower()}@example.com'
print(f'''
    Tu nuevo email generado por el sistema es:
    {email_generado}
    Felicidades!!''')
