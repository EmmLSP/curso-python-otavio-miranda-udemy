"""
Exercicio 016
Faca um programa que peca uma data no formato dd/mm/aaaa
e determine se a mesma é uma data valida.
"""

from datetime import date

dia = int(input('Digite qual é o dia: '))
if 1 <= dia <= 31:
    mes = int(input('Digite qual é o mes: '))
    if mes == 2 and dia > 28:
        print('Dia invalido para fevereiro')
    else:
        if 1 <= mes <= 12:
            ano = int(input('Digite qual é o ano: '))
            cem_anos = date.today().year - 100
            ano_atual = date.today().year
            if cem_anos <= ano <= ano_atual:
                print(f'{dia:02}/{mes:02}/{ano}')
                print('É uma data válida!')
            else:
                print(f'Ano invalido, ano precisa ser entre {cem_anos} e {ano_atual}')
        else:
            print('Mes invalido, mes precisa ser entre 1 e 12')
else:
    print('Dia invalido, dia precisa ser entre 1 e 31')
