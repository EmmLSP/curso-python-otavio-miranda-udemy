"""
Exercicio 042
Elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu preco
normal e condicao de pagamento:

- à vista dinheiro / cheque - 10% de desconto
- à vista no cartao: 5% de desconto
- em ate 2x no cartao: preco normal
- 3x ou mais no cartao: 20% juros
"""
print(f'{' LOJAS GUANABARA ':=^40}')
preco_str = input('Preco das compras: R$ ')
if preco_str.replace('.', '').isdigit():
    preco = float(preco_str)
    print('FORMAS DE PAGAMENTO')
    print('[ 1 ] à vista dinheiro/cheque')
    print('[ 2 ] à vista no cartao')
    print('[ 3 ] 2x no cartao')
    print('[ 4 ] 3x ou mais no cartao')
    opcao_str = input('Qual e a opcao? ')
    if opcao_str.isdigit():
        opcao = int(opcao_str)
        total = 0 # boa pratica, inicializar variavel fora do if else
        if opcao == 1:
            total = preco - (preco * 10 / 100) # 10% de desconto
        elif opcao == 2:
            total = preco - (preco * 5 / 100) # 5% de desconto
        elif opcao == 3:
            parcelamento = preco / 2
            total = preco
            print(f'Sua compra sera parcelada em 2x de R${parcelamento:.2f} SEM JUROS')
        elif opcao == 4:
            total = preco + (preco * 20 / 100) # 20% de juros
            parcelas = int(input('Quantas parcelas? '))
            parcelamento = total / parcelas
            print(f'Sua compra sera parcelada em {parcelas}x de R${parcelamento:.2f} COM JUROS')
        else:
            print('OPCAO INVALIDA de pagamento. Tente novamente.')
        if total > 0:
            print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
    else:
        print('Opcao precisa ser um numero inteiro')
else:
    print('Preco precisa ser um numero flutuante ou inteiro')
