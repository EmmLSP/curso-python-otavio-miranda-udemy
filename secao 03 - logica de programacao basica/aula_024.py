# Operadores in e not in

# in - esta entre
# not in - nao esta entre

# Strings sao iteraveis
#  0 1 2 3 4 5
#  O t a v i o
# -6-5-4-3-2-1

nome = 'Otávio'

""" print(nome[2])
print(nome[-4])

# expressao que tem como retorno 
# um resultado booleano
print('á not in nome:', 'á' not in nome)
print('á in nome:', 'á' in nome)
print('vio not in nome:', 'vio' not in nome)
print('vio in nome:', 'vio' in nome)
print('z not in nome:', 'z' not in nome)
print('z in nome:', 'z' in nome)
print('zero not in nome:', 'zero' not in nome)
print('zero in nome:', 'zero' in nome)


print('-' * 15)
print('0 1 2 3 4 5')
print(nome[0], end=' ')
print(nome[1], end=' ')
print(nome[2], end=' ')
print(nome[3], end=' ')
print(nome[4], end=' ')
print(nome[5])
print('-' * 15)

print('-6-5-4-3-2-1')
print(nome[-6], end=' ')
print(nome[-5], end=' ')
print(nome[-4], end=' ')
print(nome[-3], end=' ')
print(nome[-2], end=' ')
print(nome[-1])
print('-' * 15) """

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encotrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
