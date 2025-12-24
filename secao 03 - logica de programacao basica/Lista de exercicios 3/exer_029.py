"""
Exercicio 029
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$1.99, 
com cerca de 10 caixas. Para agilizar o  calculo de quanto cada 
cliente deve pagar ele desenvolveu  uma tabela que contem o numero 
de itens que o cliente  comprou e ao lado o valor da conta. Desta 
forma a atendente do caixa precisa apenas contar quantos itens o 
cliente esta levando e olhar na tabela de precos. Voce foi contratado 
para desenvolver o programa que monsta essa tabela de precos que 
contera os precos de 1 ate 50 produtos. 
Conforme exemplo abaixo:

Lojas Quase Dois - Tabela de Precos
1 - R$ 1.99
2 - R$ 3.98
...
50 R$ 99.50
"""

print('Loja Quase Dois - Tabela de Precos:')
print('-' * 35)
for itens in range(1, 51):
    print(f'{itens:2} - R${1.99 * itens:6.2f}')
print('-' * 35)
