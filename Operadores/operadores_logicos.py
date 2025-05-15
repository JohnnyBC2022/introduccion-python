print('*** Operador AND ***')

# Devuelve True si ambos valores son verdaderos
condicion1 = True
condicion2 = False

resultado = condicion1 and condicion2
print(f'Resultado {condicion1} y {condicion2} es: {resultado}')

print('*** Operador OR ***')
# Devuelve True si cualquiera de los valores es verdadero
condicion3 = True
condicion4 = False

resultado = condicion3 or condicion4
print(f'Resultado {condicion3} y {condicion4} es: {resultado}')

print('*** Operador NOT ***')
# Cambia el valor de un booleano
usuario_valido = True

print(f'Usuario válido: {usuario_valido}')
print(f'Invertimos valor: {not usuario_valido}')
