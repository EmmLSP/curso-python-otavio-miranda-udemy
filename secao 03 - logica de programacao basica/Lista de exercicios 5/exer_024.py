"""
Exercicio 024
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso sera
guardado em um dicionario, incluindo o total de gols feitos
durante o campeonato.

Aprimore o desafio 022 para que ele funcione
com varios jogadores, incluindo um sistema de
visualizacao de detalhes do aproveitamento de
cada jogador.
"""

from time import sleep

time = list()
jogador = dict()
partidas = list()
while True:
    print('-' * 30)
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(total):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

# Cabecalho
print('-' * 40)
# print(f'{'cod ':<4}{'jogador':<15}{'gols':<15}{'total':<8}')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        print('Finalizando...')
        sleep(1)
        break
    # if busca >= len(time) -> mostra msg de erro
    if 0 <= busca < len(time):
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
        for k, v in enumerate(time[busca]['gols']):
            print(f'    No jogo {k+1} fez {v} gols')
    else:
        print(f'Erro! Nao existe jogador com codigo {busca}! Tente novamente')
    print('-' * 40)

print('<<< VOLTE SEMPRE >>>')
