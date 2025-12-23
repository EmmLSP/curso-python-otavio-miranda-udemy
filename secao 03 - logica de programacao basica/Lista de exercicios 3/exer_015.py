"""
Exercicio 015
A serie de Fibonacci é formada pela sequencia
1, 1, 3, 5, 8, 13, 21, 34, 55,... Faca um
programa que gere a serie ate o n-ésimo termo.
"""

enesimo_termo = int(input('Digite o n-ésimo termo de uma sequencia de Fibonacci: '))

primeiro_termo = 1
segundo_termo = 1

print(f'{primeiro_termo}, {segundo_termo}, ', end='')

for n in range(2, enesimo_termo):
    primeiro_mais_segundo = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = primeiro_mais_segundo
    if n < enesimo_termo - 1:
        print(f'{primeiro_mais_segundo}, ', end='')
    else:
        print(f'{primeiro_mais_segundo}')
