"""
Exercicio 024
Crie um programa que leia a idade e o sexo de varias
pessoas. A cada pessoa cadastrada, o programa devera
perguntar se o usuario quer ou nao continuar.
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos. 
"""

from time import sleep

print('-' * 30)
print(F'{'CADASTRE UMA PESSOA':^30}')
print('-' * 30)

pes = 1
maior_18 = homens_cadast = mulheres_menor_20 = 0
while True:
    print(f'Pessoa {pes}:')
    
    while True:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Idade precisa ser maior que zero')
            continue
        break
    while True:
        sexo = input('Sexo? [M/F] ').upper()
        if sexo not in 'MF':
            print('Sexo invalido! Digite \'F\' ou \'M\'')
            continue
        break
    
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens_cadast += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
    pes += 1

    print('-' * 30)
    while True:
        resp = input('Quer continuar? [S/N] ').upper()
        if resp not in 'SN':
            print('Resposta invalida! Digite \'S\' ou \'N\'')
            continue
        break

    if resp == 'N':
        print('\nEncerrando...')
        sleep(1)
        break

    print('-' * 30)
    print(F'{'CADASTRE MAIS UMA PESSOA':^30}')
    print('-' * 30)

print('-=' * 5, ' FIM DO PROGRAMA ', '-=' * 5)
if maior_18 > 0:
    print(f'Total de pessoas com mais de 18 anos: {maior_18}')
else:
    print('Nenuma pessoa com mais de 18 anos foi cadastrado')
if homens_cadast == 1:
    print(f'Ao todo temos {homens_cadast} homem cadastrado')
elif homens_cadast > 1:
    print(f'Ao todo temos {homens_cadast} homens cadastrados')
else:
    print('Nenhum homem foi cadastrado')
if mulheres_menor_20 == 1:
    print(f'E temos {mulheres_menor_20} mulher com menos de 20 anos')
elif mulheres_menor_20 > 1:
    print(f'E temos {mulheres_menor_20} mulheres com menos de 20 anos')
else:
    print('Nenhuma mulher foi cadastrada.')
