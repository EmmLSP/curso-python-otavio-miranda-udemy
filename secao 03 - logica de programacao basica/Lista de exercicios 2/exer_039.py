"""
Exercicio 039
A confederacao Nacional de Natacao precisa de
um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a
idade:

- Ate 9 anos: MIRIM
- Ate 14 anos: INFANTIL
- Ate 19 anos: JUNIOR
- Ate 25 anos: SENIOR
- Acima: MASTER
"""

from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificacao: MIRIM')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 25:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
