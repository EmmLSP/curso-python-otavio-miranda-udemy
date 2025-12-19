"""
Exercicio 037
Faca um programa que leia o ano de nascimento de 
um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar no servio militar
- Se e a hora de se alistar
- Se ja passou do tempo do alistamento

Seu programa tambem devera mostrar o tempo que 
falta ou que passou do prazo.
"""

from datetime import date

ano_atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano_atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')
if idade < 18:
    menor_18 = 18 - idade
    if menor_18 == 1:
        print(f'Ainda falta {menor_18} ano para o alistamento')
    else:
        print(f'Ainda faltam {menor_18} anos para o alistamento')
    print(f'Seu alistamento sera em {ano_atual + menor_18}.')
elif idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
else:
    maior_18 = idade - 18
    if maior_18 == 1:
        print(f'Voce ja deveria ter se alistado ha {maior_18} ano')
    else:
        print(f'Voce ja deveria ter se alistado ha {maior_18} anos')
    print(f'Seu alistamento foi em {ano_atual - maior_18}.')
