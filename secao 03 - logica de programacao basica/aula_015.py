# Usando a funcao input para coletar dados do usuario

# input sempre retorna uma string
# e preciso fazer coerçao, conversao de tipos

# nome = input('Qual é o seu nome? ')
# print(f'Seu nome é {nome}')
# print(f'Seu nome é {nome=}')
# check no meio do camainho entre os codigos
# entrada do usuario

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma dos numeros é {int_numero_1 + int_numero_2}')
