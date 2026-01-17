"""
Exercicio 021
Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os (com idade) em um
dicionario se por acaso a CPTS for diferente de zero,
o dicionario recebera tambem o ano de contratacao e o
salario. Calcule e acrescente, alem da idade, com 
quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = (datetime.now().year) - nasc
dados['cpts'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['cpts'] != 0:
    dados['contratacao'] = int(input('Ano de contratacao: '))
    dados['salario'] = float(input('Salario: R$ '))
    # dados['aposentadoria'] = (dados['contratacao'] + 35) - nasc
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
