"""
Exercicio 041
Faca um programa que receba o valor de uma divida e
mostre uma tabela com os seguintes dados: valor da
divida, valor dos juros, quantidade de parcelas e
valor da parcela.
- Os juros e a quantidade de parcelas seguem a tabela
abaixo:

1 parcela   ==  0% juros
3 parcelas  == 10% juros
6 parcelas  == 15% juros
9 parcelas  == 20% juros
12 parcelas == 25% juros

Exemplo de saida do programa:
Valor da Divida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela
-----------------------------------------------------------------------------
R$ 1.000,00       0                 1                        R$ 1.000,00
R$ 1.100,00       100               3                        R$   366,00
R$ 1.150,00       150               6                        R$   191,17
-----------------------------------------------------------------------------

valor_divida = 1000
print(valor_divida)
valor_divida = 1000
valor_divida += (valor_divida * 10 / 100)
print(valor_divida / 3)
valor_divida = 1000
valor_divida += (valor_divida * 15 / 100)
print(valor_divida / 6)
valor_divida = 1000
valor_divida += (valor_divida * 20 / 100)
print(valor_divida / 9)
valor_divida = 1000
valor_divida += (valor_divida * 25 / 100)
print(valor_divida / 12)

"""

valor_divida = float(input('Digite o valor da divida: R$ '))
valor_temp = valor_divida
juros = 5
parcelas = 0

print('Valor da Divida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela')
print('-' * 77)

print(f'R$ {valor_divida:<14.2f}{'0':<19}{'1':<25}R${valor_divida:8.2f}')

for n in range(2, 6):
    juros += 5
    valor_juros = valor_divida * juros / 100
    valor_divida += valor_juros
    parcelas += 3
    valor_parcela = valor_divida / parcelas
    print(f'R$ {valor_divida:<14.2f}{valor_juros:<19}{parcelas:<25}R${valor_parcela:8.2f}')
    valor_divida = valor_temp # 1000
