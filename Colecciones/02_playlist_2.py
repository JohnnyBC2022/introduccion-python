print('*** Playlist Dinámica ***')

# Creación de una lista vacía
lista_reproduccion = []
numero_canciones = int(input('¿Cuántas canciones quieres añadir a la lista?'))

# Iteramos cada elemento de la lista para añadir un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Escribe la canción {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabético
lista_reproduccion.sort()
# lista_reproduccion.sort(reverse=True) Orden Descendente

# Mostrar la lista de canciones
print(f'\n Lista de Reproducción en Orden Alfabético: ')

for cancion in lista_reproduccion:
    print(f'  - {cancion}')
