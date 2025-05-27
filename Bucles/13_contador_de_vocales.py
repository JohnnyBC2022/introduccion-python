cadena = input('Escribe un mensaje para contar sus vocales: ')
vocales = "aeiouAEIOU"
contador = 0

for caracter in cadena:
    if caracter in vocales:
        contador += 1

print(contador)
