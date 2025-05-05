# Manejo de subcadenas

cadena = 'Hola, mundo!'

# Obtenemos los primeros 5 caracteres "Hola" (slicing), hay que tener en cuenta que en este caso, la ","
# del último índice no se incluye
subcadena1 = cadena[0:4]  # [inicio: fin(exclusivo)]
print(subcadena1)

# Obtención de la subcadena "mundo"
subcadena2 = cadena[6:11]
print(subcadena2)
