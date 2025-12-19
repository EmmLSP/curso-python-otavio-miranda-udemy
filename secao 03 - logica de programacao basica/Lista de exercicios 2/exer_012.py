"""
Exercicio 012
Faca um programa para o calculo de uma folha de pagamento, sabendo 
que os descontos sao do imposto de renda, que depende do salario bruto 
(conforme tabela abaixo) e 3% para o sindicato e que o FGTS corresponde 
a 11% do salario bruto, mas nao e descontado (é a empresa que deposita).
O INSS e descontado e corresponde a 8% do valor do salario bruto.
O salario liquido corresponde ao salario bruto menos os descontos.
O programa devera pedir ao usuario o valor da sua hora e quantidade de 
horas trabalhadas no mes.
Tabela do IR:
- salario bruto ate 900 (inclusive) - isento
- salario bruto ate 1500 (inclusive) - desconto de 5%
- salario bruto ate 2500 (inclusive) - desconto de 10%
- salario bruto acima de 2500 - desconto de 20%
Imprima os seguintes valores: salario bruto, ir, inss, fgts, total de
descontos e o salario liquido.
"""

valor_hora = float(input('Digite quanto é o seu valor/hora: R$ '))
qtd_horas = int(input('Digite a quantidade de horas trabalhadas no mes: '))
salario_bruto = valor_hora * qtd_horas
desconto_ir = 0
if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20
ir = (salario_bruto / 100) * desconto_ir
inss = (salario_bruto / 100) * 10
fgts = (salario_bruto / 100) * 11
sindicato = (salario_bruto / 100) * 5
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos
print('-' * 40)
print(f'{'FOLHA DE PAGAMENTO':^40}')
print('-' * 40)
print(f'Salario Bruto ({valor_hora:05.2f} * {qtd_horas})   R${salario_bruto:8.2f}')
print(f'(-) IR ({desconto_ir:02}%)                  R${ir:8.2f}')
print(f'(-) INSS (10.0%)              R${inss:8.2f}')
print(f'FGTS (11.0%)                  R${fgts:8.2f}')
print(f'Total de descontos            R${total_descontos:8.2f}')
print(f'Salario Liquido               R${salario_liquido:8.2f}')
print('-' * 40)
