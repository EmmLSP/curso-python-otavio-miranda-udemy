"""
Exercicio 13
Faca um programa que leia a largura e a altura de uma
parede em metros, calcule a sua area e a quantidade de
tinta necessaria para pinta-la, sabendo que cada litro
de tinta, pinta uma area de 2m².
"""

larg_str = input('Largura da parede: ')
largura = float(larg_str)
alt_str = input('Altura da parede: ')
altura = float(alt_str)
area = largura * altura
qtd_tinta = area / 2
qtd_tinta_l = int(qtd_tinta // 1)
qtd_tinta_ml = (qtd_tinta - qtd_tinta_l) * 1000
print(f'Sua parede tem a dimensao de {largura}x{altura} e sua area é de {area}m²')
print(f'Para pintar essa parede, voce precisara de {qtd_tinta}l de tinta.')
print(f'Para pintar essa parede, voce precisara de {qtd_tinta_l}l e {round(qtd_tinta_ml)}ml de tinta.')
