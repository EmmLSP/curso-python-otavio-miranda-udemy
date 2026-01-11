"""
Exercicio 012
Crie um programa onde o usuario digite uma
expressao qualquer que use parenteses. Seu
aplicativo devera analisar se a expressao
passada esta com os parenteses abertos e
fechados na ordem correta.
"""

pilha = []
expressao = input('Digite a expressao: ')
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() # remove ultimo elemento da lista
        else:
            pilha.append(')')
            break
print('-=' * 30)
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta errada!')
