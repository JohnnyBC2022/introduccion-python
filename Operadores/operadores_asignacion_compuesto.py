print('*** Operadores de asignación compuestos ***')
a, b = 10, 15
print(f'Valor inicial de a: {a} \nValor inicial de b: {b}')

# Operador compuesto de suma +=
a += b  # a = a + b
print(f'Operador a += b es: {a}')  # 10 + 15

# Operador compuesto de resta -=
a = 10  # reiniciamos el valor de a
a -= b  # a = a - b
print(f'Operador a -= b es: {a}')  # 10 - 15

# Operador compuesto de multiplicación *=
a = 10  # reiniciamos el valor de a
a *= b  # a = a * b
print(f'Operador a *= b es: {a}')  # 10 * 15

# Operador compuesto de división *=
a = 10  # reiniciamos el valor de a
a /= b  # a = a / b
print(f'Operador a /= b es: {a}')  # 10 / 15
