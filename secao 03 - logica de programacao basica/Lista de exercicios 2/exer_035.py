"""
Exercicio 035
Escreva um programa que leia um numero inteiro
qualquer e peca para o usuario escolher qual 
sera a base de conversao:

- 1 para binario
- 2 para octal
- 3 para hexadecimal
"""

num = int(input('Digite um numero inteiro: '))
print('-' * 40)
print('''Escolha uma das bases para conversao
----------------------------------------
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
print('-' * 40)
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print(f'{num} convertido em BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido em OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido em HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opcao invalida. Tente novamente.')
