print('*** Repetición de un mensaje ***')

mensaje = input('Escribe un mensaje a repetir: ')
numero_de_repeticiones = int(input('Escribe el número de repeticiones: '))

# iterar sobre el rango de repeticiones
# si la variable que almacena el índice de la repetición no lo vamos a usar se puede utilizar esta sintaxis _

for _ in range(numero_de_repeticiones):
    # print(_)
    print(mensaje)
