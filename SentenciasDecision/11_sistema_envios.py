print('*** Sistema de envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitar los valores de destino y peso
destino = input('Escribe el tipo de envío (nacional o internacional): ')
peso = float(input('Introduce el peso del paquete (en Kg): '))

coste_envio = None  # Definimos la variable de coste de envío

# Cálculo del coste de envío
if destino.lower() == 'nacional':
    coste_envio = peso * TARIFA_NACIONAL
elif destino.lower() == 'internacional':
    coste_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Tipo de envío no válido. Escribe nacional o internacional')

# Mostra el costo de envío sólo si es un valor válido
if coste_envio is not None:
    print(f'''El coste de envío del paquete con un peso de {peso} Kg.
con destino {destino}
tiene un coste de {coste_envio:.2f} €
    ''')
