# 1. Paréntesis (): Los paréntesis tiene la mayor precedencia.
# 2. Exponente **: Este operador calculca la potencia de un número.
# 3. Unitario +, -: Estos operadores realizan operaciones unitarias de asignación de signo positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones matemáticas.
# 6. Comparaciones (==, != , <, >, <=, >=)
# 7. Operadores lógicos not, and, or.
# 8. Asignación (=, +=, -=, *=, /=, entre otros)
from operadores_comparacion import resultado

resultado = 12 / 3 + 2 * 3 - 1  # -> 4 + 6 - 1 -> 9
print(f'Resultado: {resultado}')

resultado2 = 12 / (3 + 2) * 3 - 1  # -> 12 / 5 * 3 - 1 -> 2.4 * 3 - 1 -> 6.2
print(f'Resultado: {resultado2}')
