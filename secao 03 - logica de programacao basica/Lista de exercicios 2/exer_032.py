"""
Exercicio 032
Escreva um programa que pergunte o salario de
um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$1250.00, calcule um
aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%
"""

salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <= 1250:
    aumento = (salario * 15) / 100
else:
    aumento = (salario * 10) / 100
novo_salario = salario + aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${novo_salario:.2f} agora.')
