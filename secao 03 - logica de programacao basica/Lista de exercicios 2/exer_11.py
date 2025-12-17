"""
Exercicio 11
As organizacoes Tabajara resolveram dar um aumento de salario 
aos seus colaboradores e lhe contrataram para desenvolver o 
programa que calculara os reajustes:
Faca um programa que recebe o salario de um colaborador e o 
reajuste seguindo o criterio, baseado no salario atual:
- salarios ate R$280.00 (incluindo): aumento de 20%
- salarios entre R$280.00 e R$700.00: aumento de 15%
- salarios entre R$700.00 e R$1500.00: aumento de 10%
- salarios de R$1500.00 em diante: aumento de 5%
Apos o aumento ser realizado, informar na tela:
- o percentual antes do reajuste.
- o percentual de aumento aplicado.
- O valor do aumento.
- o novo salario, apos o aumento.
"""

salario = float(input('Digite o seu salario: R$ '))

aumento = 0
if 0 <= salario <= 280:
    aumento = 20
elif 280 < salario <= 700:
    aumento = 15
elif 700 < salario <= 1500:
    aumento = 10
else:
    aumento = 5
percentual = (salario * aumento / 100)
salario_reajustado = salario + percentual

print('-' * 40)
print(f'Salario antes do reajuste...: R${salario:8.2f}')
print(f'Percentual de aumento.......: {aumento:.1f}%')
print(f'Valor do aumento............: R${percentual:8.2f}')
print(f'Salario depois do aumento...: R${salario_reajustado:8.2f}')
print('-' * 40)
