"""
Exercicio 028
Faca um programa que calcule o valor total investido por 
um colecionador em sua colecao de CDs e o valor medio gasto 
em cada um deles. O usuario devera informar a quantidade de 
CDs e o valor pago em cada um.
"""

qtd_cds = int(input('Digite a quantidade de CDs de sua colecao: '))
total = valor_medio = 0
for itens in range(qtd_cds):
    valor_cd = float(input(f'Digite o valor do CD {itens + 1}: '))
    total += valor_cd

valor_medio = total / qtd_cds
print(f'O total investido em sua coleccao foi R${total:.2f}')
print(f'O valor medio de cada CD é R${valor_medio:.2f}')
