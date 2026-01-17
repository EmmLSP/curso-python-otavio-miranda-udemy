"""
Exercicio 023
Crie um programa que leia nome, sexo e idade de
varias pessoas, guardando os dados de cada pessoa
em um dicionario e todos os dicionarios em uma
lista. No final, mostre:

A) Quantas pessoas foram cadastradas
B) A media de idade do grupo
C) Uma lista com todas as mulheres
D) Uma lista com todas as pessoas com idade acima
da media.
"""

pessoa = dict()
pessoas = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    while True:
        pessoa['idade'] = int(input('Idade: '))
        if 0 <= pessoa['idade'] <= 110:
            break
        print('ERRO! Por favor, digite idade de 0 ate 110 anos') 
    soma += pessoa['idade']
    pessoas.append(pessoa.copy()) # copia de pessoa em pessoas
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp in 'N':
        break
media = soma / len(pessoas)
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A media de idade é de {media:.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print('D) Lista das pessoas que estao acima da media:')
for p in pessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
