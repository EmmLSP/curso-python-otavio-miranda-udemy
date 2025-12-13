"""
Exercicio 22
Faca um programa que pergunte quanto voce ganha por hora 
e o numero de horas trabalhadas no mes. Calcule e mostre 
o total do seu salario no referido mes, sabendo que sao 
descontados 11% para o imposto de renda, 8% para o INSS 
e 5% para o sindicato, faca um programa que nos de:

a. salario bruto
b. quanto pagou de INSS
c. o salario liquido
d. calcule os descontos e o salario liquido, conforme 
tabela abaixo:

-----------------------
Salario Bruto      : R$
(-) IR (11%)       : R$
(-) INSS(8%)       : R$
(-) Sindicato (5%) : R$
Descontos          : R$
Salario liquido    : R$
-----------------------

Obs: Salario Bruto  - Descontos = Salario Liquido
"""

valor_hora_str = input('Digite o valor/hora trabalhado: ')
valor_hota = float(valor_hora_str)
qtd_dias_str = input('Digite a quantidade de dias trabalhados: ')
qtd_dias = int(qtd_dias_str)
salario_bruto = valor_hota * qtd_dias
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print('-' * 40)
print(f'Salario brto         : R$ {salario_bruto:8.2f}')
print(f'(-) IR (11%)         : R$ {ir:8.2f}')
print(f'(-) INSS (8%)        : R$ {inss:8.2f}')
print(f'(-) Sindicato (5%)   : R$ {sindicato:8.2f}')
print(f'Descontos            : R$ {descontos:8.2f}')
print(f'Salario liquido      : R$ {salario_liquido:8.2f}')
print('-' * 40)
