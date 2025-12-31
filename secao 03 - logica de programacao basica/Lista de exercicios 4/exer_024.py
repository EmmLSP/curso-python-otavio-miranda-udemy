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

pessoa = 1
maior_igual_18 = total_homens = total_mulheres = mulheres_menos_20 = 0
while True:
    print(f'Pessoa {pessoa:03}:')
    while True:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Idade precisa ser maior que zero')
            continue
        break
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo? [M/F] ').strip().upper()[0]
        if sexo not in 'MF':
            print('Sexo invalido! Digite \'F\' ou \'M\'')
            continue
    
    if idade >= 18:
        maior_igual_18 += 1
    
    if sexo == 'M':
        total_homens += 1

    if sexo == 'F':
        total_mulheres += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    pessoa += 1

    print('-' * 30)
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp not in 'SN':
            print('Entrada invalida! Digite \'S\' ou \'N\'')
            continue
        break

    if resp == 'N':
        print('\nEncerrando...')
        sleep(1)
        break

    print('-' * 30)
    print(F'{'CADASTRE UMA PESSOA':^30}')
    print('-' * 30)

print(f'{' FIM DO PROGRAMA ':=^30}')
if maior_igual_18 > 0:
    print(f'Total de pessoas com 18 anos ou mais: {maior_igual_18}')
else:
    print('Nenuma pessoa com mais de 18 anos foi cadastrado')
if total_homens == 1:
    print(f'Ao todo temos {total_homens} homem cadastrado')
elif total_homens > 1:
    print(f'Ao todo temos {total_homens} homens cadastrados')
else:
    print('Nenhum homem foi cadastrado')
if total_mulheres > 0:
    if total_mulheres == 1:
        print(f'E temos temos {total_mulheres} mulher cadastrada')
    else:
        print(f'E temos {total_mulheres} mulheres cadastradas')
    if mulheres_menos_20 == 1:
        print(f'Sendo {mulheres_menos_20} mulher com menos de 20 anos')
    elif mulheres_menos_20 > 1:
        print(f'Sendo {mulheres_menos_20} mulheres com menos de 20 anos')
    else:
        print('E nenhuma mulher menor de 20 anos foi cadastrada')
else:
    print('Nenhuma mulher foi cadastrada.')
