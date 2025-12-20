# while e break - Estrutura de repetição (Parte 1)

"""
Repetições 
While (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
break -> dentro de um laco procura o laco mais proximo
para interromper
"""

condicao = True
cont = 0
limite = 5
nomes = ''
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')
    nomes += nome + ' '
    if cont == limite - 1:
        break
    cont += 1
print('-' * 20)
print(nomes)
print('Fim do Laco')

print()

nomes = ''
while True:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')
    if nome.lower() == 'sair':
        break
    nomes += nome + ' '
print('-' * 20)
print(nomes)
print('Fim do Laco')
