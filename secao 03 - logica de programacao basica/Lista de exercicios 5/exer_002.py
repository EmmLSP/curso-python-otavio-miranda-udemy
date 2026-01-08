"""
Exercicio 002
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol de 2017,
na ordem de colocacao. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que posicao na tabela esta o time da Chapecoense.
"""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
    'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 
    'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense',
    'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

pontos = (72, 63, 62, 62, 57, 56, 56, 54, 54, 53, 51, 
    50, 50, 47, 45, 43, 43, 42, 39, 36)


print(f'{'\nCAMPEONATO BRASILEIRO SERIE A 2017':^35}')
print('-' * 36)
print(f'{'Pos':<6}{'Time':<21}{'Pontos':<9}')
print('-' * 36)
for pos, time in enumerate(times):
    print(f'{pos+1:<6}', end='')
    if pos <= 4:
        print(f'\033[1;32m{time:<21}\033[m{pontos[pos]:<9}')
    elif pos == 7: 
        print(f'\033[1;34m{time:<21}\033[m{pontos[pos]:<9}')
    elif 4 < pos <= 15: 
        print(f'\033[1;33m{time:<21}\033[m{pontos[pos]:<9}')
    else:
        print(f'\033[1;31m{time:<21}\033[m{pontos[pos]:<9}')
print('-' * 36)
print()

print('-=' * 18)
print(f'Lista de times do Brasileirao {times}')
print('-=' * 18)
print(f'Os 5 primeiros são {times[:5]}')
print('-=' * 18)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-=' * 18)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 18)
print(f'A Chapecoense esta na {times.index('Chapecoense') + 1}ª posicao do campeonato')
print('-=' * 18)
