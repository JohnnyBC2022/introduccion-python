print('*** Playlist Simple ***')

# Creación de una lista vacía
lista_reproduccion = []

# Añadir canciones
lista_reproduccion.append('Dream On - Aerosmith')
lista_reproduccion.append('Staying Alive - Bee Gees')
lista_reproduccion.append('Hotel California - Eagles')

# Ordenar la lista en orden alfabético
lista_reproduccion.sort()

# Mostrar la lista de canciones
print(f'\n Lista de Reproducción en Orden Alfabético: ')

for cancion in lista_reproduccion:
    print(f'  - {cancion}')
