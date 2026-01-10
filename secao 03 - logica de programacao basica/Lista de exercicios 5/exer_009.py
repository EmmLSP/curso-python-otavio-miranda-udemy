"""
Exercicio 009
Crie um programa onde o usuario possa digitar
cinco valores numericos e cadastre-os em uma
lista, ja na posicao correta de inserção
(sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

numeros = []
for c in range(5):
    num = int(input(f'Digite um valor: '))
    if c == 0 or num > numeros[len(numeros) - 1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {numeros}')
