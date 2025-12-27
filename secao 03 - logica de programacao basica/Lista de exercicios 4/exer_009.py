"""
Exercicio 009
Crie um programa que leia o ano de nascimento de sete
pessoas. No final, mostre quantas pessoas ainda nao 
atingiram a maioridade e quantas ja maiores.
Considerar a maioridade com 21 anos.
"""

from datetime import date

ano_atual = date.today().year
menores = maiores = 0
idades = ''
for p in range(1, 8):
    nasc = int(input(f'Em que ano {p}° pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        idades += f'\033[1;32m{idade}\033[m '
        maiores += 1
    else:
        idades += f'\033[1;33m{idade}\033[m '
        menores += 1
print(f'Idades: {idades}')
print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E tambem tivemos {menores} pessoas menores de idade')
