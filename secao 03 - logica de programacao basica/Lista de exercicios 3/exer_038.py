"""
Exercicio 038
Um funcionario de uma empresa recebe aumento salarial
anualmente:
Sabe-se que:
a. Esse funcionario foi contratado em 1995, com salario
inicial de R$ 1.000.00.
b. Em 1996 recebeu aumento de 1.5% sobre seu salario
inicial.
c. A partir de 1997 (inclusive), os aumentos sempre 
correspondem ao dobro do percentual do ano anterior.
Faca um programa que determine o salario atual desse
funcionario. Apos concluir isto, altere o programa
permitindo que o usuario digite o salario inicial do
funcionario.
"""

from datetime import date

ano_atual = date.today().year
percentual = 1.5
print(f'Ano atual: {ano_atual}')
salario_1995 = 1000
salario_1996 = salario_1995 + (salario_1995 * percentual / 100)
print(f'Salario em 1995 - R${salario_1995:.2f} com percentual 0.0%')
print(f'Salario em 1996 - R${salario_1996:.2f} com percentual {percentual:5.1f}%')
salario = salario_1996
ano = 1997
while ano <= ano_atual:
    percentual *= 2
    salario += (salario * percentual / 100)
    print(f'Salario em {ano} - R${salario:.2f} com percentual {percentual:5.1f}%')
    ano += 1
