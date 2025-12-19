"""
Exercicio 034
Escreva um programa para aprovar um emprestimo 
bancario para compra de uma casa. O programa vai
perguntar o valor da casa, o salario do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestacao mensal, sabendo que 
ela nao pode exceder 30% do salario ou entao sera
negado.
"""

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'\033[1;33mPara pegar uma casa de \033[mR${casa:,.2f}\033[1;33m', end='')
print(f' em {anos} anos a prestacao sera de\033[m R${prestacao:.2f}')
if prestacao <= minimo: # prestacao <= 30% salario
    print('\033[1;32mEmprestimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmprestimo NEGADO!\033[m')
