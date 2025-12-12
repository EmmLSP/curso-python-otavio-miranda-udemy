"""
Exercicio 15 
Faca um algoritmo que leia o salario de um funcionario 
e mostre seu novo salario, com 15% de aumento.
"""

salario_str = input('Qual é o salario do funcionario? R$ ')
salario = float(salario_str)
novo_salario = salario + (salario * 15 / 100)
print(f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}')
