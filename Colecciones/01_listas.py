print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]

# Accedemos a un elemento por índice
print(f'Accedemos al valor del índice 4: {mi_lista[4]}')

# Modificar un elemento de la lista
print(f'Accedemos al valor del índice 1: {mi_lista[1]}')
mi_lista[1] = 10
print(f'Accedemos al valor del índice 1 modificado: {mi_lista[1]}')

# Añadir un nuevo elemento a la lista (lo hace al final)
mi_lista.append(6)
print(mi_lista)

# Eliminar un elemento de la lista
del mi_lista[2]
print(mi_lista)

# Longitud de la lista
print(f'Tamaño de la lista: {len(mi_lista)}')
