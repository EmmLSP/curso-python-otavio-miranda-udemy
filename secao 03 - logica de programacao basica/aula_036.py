# Operadores de atribuição com operadores aritméticos

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0
while contador <= 10:
    contador += 1
    print(contador)
print('Acabou')

print('\nOperador com + -> += -> soma de inteiros')
print('contador = 11')
contador += 1 # 11 + 1
print('contador += 1')
print('11 += 1 == 12')
print(contador, type(contador)) # inteiro -> 12

print('\nOperador + com string -> += -> contatenacao')
print('contador = \'1\'')
print('contador += \'2\'')
print('\'1\' + \'2\' = \'12\'')

contador = '1'
contador += '2' # '1' + '2'
print(contador, type(contador)) # string -> '12'

print('\nOperador * com string -> *= -> repeticao')
print('contador = 10')
print('contador *= \'2\'')
print('\'2\' * 10')

contador = 10
contador *= '2' # contador *= '2' -> 10x
print(contador) # * -> '2222222222'


print('\nOperador com % -> %= -> resto igual a 0 -> PAR')
contador = 10
print('numero:', contador)
contador %= 2
print('resto:',contador) # 0
if contador == 0:
    print('PAR')
else:
    print('IMPAR')

print('\nOperador com % -> %= -> resto igual a 1 -> IMPAR')
contador = 11
print('numero:',contador)
contador %= 2
print('resto:',contador) # 1
if contador == 0:
    print('PAR')
else:
    print('IMPAR')

print('\nOperador com ** -> **= -> potenciacao')
contador = 2
contador **= 10
print('contador **= 10')
print('2 **= 10 = ', end='')
print(contador)

print('\nOperador com / -> **= -> divisao -> return float')
contador = 10
contador /= 2
print('contador /= 2')
print('10 /= 2 = ', end='')
print(contador)

print('\nOperador com // -> **= -> divisao inteira -> return int')
contador = 10
contador //= 2
print('contador //= 2')
print('10 //= 2 = ', end='')
print(contador)
