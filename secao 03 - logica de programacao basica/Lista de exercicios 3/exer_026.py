"""
Exercicio 026
Numa eleição existem 3 candidatos. Faca um programa
que peca o numero total de eleitores. Peca para cada
eleitor votar e ao final mostrar o numero de votos de
cada candidato.
"""

eleitores = int(input('Digite a quantidade de eleitores: '))

candidato_a = 0
candidato_b = 0
candidato_c = 0

cont = maior = 0
while cont < eleitores:
    eleitor = input('Digite em que candidato voce vai votar? [a, b ou c] ').lower()

    if eleitor not in 'abc':
        print('Candidato invalido! Vote no candidato \'a\', \'b\' ou \'c\'')
        continue
    elif eleitor.isalpha():
        if eleitor == 'a':
            print('Voto para o candidato A')
            candidato_a += 1
        elif eleitor == 'b':
            print('Voto para o candidato B')
            candidato_b += 1
        elif eleitor == 'c':
            print('Voto para o candidato C')
            candidato_c += 1
        cont += 1
    else:
        print('Digite um letra para cada candidato: a, b ou c')

print(f'Candidato A = {candidato_a} votos')
print(f'Candidato B = {candidato_b} votos')
print(f'Candidato C = {candidato_c} votos')
