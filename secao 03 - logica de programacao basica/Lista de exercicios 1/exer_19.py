"""
Exercicio 19
Faca um programa que pergunte quanto voce ganha por hora
e o numero de horas trabalhadas no mes. Calcule e mostre
o total do seu salario no referido mes.
"""

valor_hora_str = input('Digite o valor/hora do trabalho: ')
valor_hora = float(valor_hora_str)
qtd_horas_str = input('Digite a quantidade de horas trabalhadas no mes: ')
qtd_horas = int(qtd_horas_str)
salario_total = valor_hora * qtd_horas
print(f'O salario total no final do mes será de R${salario_total:.2f}')
