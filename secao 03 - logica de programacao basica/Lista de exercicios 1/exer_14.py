"""
Exercicio 14 
Faca um algoritmo que leia o preco de um produto
e mostre seu novo preco com 5% de desconto.
"""

produto_str = input('Qual é o preco do produto? R$ ')
produto = float(produto_str)
novo_preco = produto - (produto * 5 / 100)
print(f'O produto que custava R${produto:.2f}, na promocao com desconto de 5%, vai custar R${novo_preco:.2f}')
