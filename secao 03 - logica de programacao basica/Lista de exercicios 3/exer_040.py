"""
Exercicio 040
Foi feita uma estatistica em cinco cidades brasileiras
para coletar dados sobre acidentes de transito. Foram
obtidos os seguintes dados:
- Codigo da cidade
- Numero de veiculos de passeio (em 1999)
- Numero de acidentes de transito com vitimas (em 1999)
deseja-se saber:
a. Qual o maior e menor indice de acidentes de transito e
a que cidade pertence
b. Qual a media de veiculos nas cinco cidades juntas
c. Qual a media de acidentes de transito nas cidades com
menos de 2000 veiculos de passeio.
"""

maior_indice_acidentes = menor_indice_acidentes = 0
cidade_menor_indice = cidade_maior_indice = 0
soma_veiculos = media_veiculos = 0
soma_acidentes = media_acidentes = 0
maior_indice_cidade = menor_indice_cidade = ''
estatisticas = 'codigo | Cidade              | veiculos (em 1999) | acidentes de transito (em 1999)\n'
for c in range(1, 6):  
    while True:
        cidade = input(f'Digite o nome da cidade {c}: ')
        if len(cidade) < 3 :
            print('Cidade precisa ter no minimo 3 digitos')
            continue
        break

    while True:
        codigo = int(input(f'Digite o codigo da cidade de {cidade}: '))
        if len(str(codigo)) < 4 or len(str(codigo)) > 4 or codigo <= 0:
            print('Codigo precisa ter 4 digitos maior que zero')
            continue
        break

    while True:
        veiculos = int(input(f'Digite o numero de veiculos de {cidade} (em 1999) : '))
        if veiculos <= 0:
            print('A quantidade de veiculos precisa ser maior que zero')
            continue
        break

    while True:
        acidentes = int(input(f'Digite o numero de acidentes de transito de {cidade} (em 1999) : '))
        if acidentes <= 0:
            print('A quantidade de acidentes precisa ser maior que zero')
            continue
        break

    soma_veiculos += veiculos
    if veiculos < 2000:
        soma_acidentes += acidentes

    if c < 5:
        estatisticas += f'{codigo:<6} | {cidade:<19} | {veiculos:<18} | {acidentes:<8}\n'
    else:
        estatisticas += f'{codigo:<6} | {cidade:<19} | {veiculos:<18} | {acidentes:<8}'

    if c == 1:
        maior_indice_acidentes = menor_indice_acidentes = acidentes
        maior_indice_cidade = menor_indice_cidade = cidade
    else:
        if acidentes > maior_indice_acidentes:
            maior_indice_acidentes = acidentes
            maior_indice_cidade = cidade
        if acidentes < menor_indice_acidentes:
            menor_indice_acidentes = acidentes
            menor_indice_cidade = cidade

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes / 5

print('-' * 90)
print(estatisticas)
print('-' * 90)
print(f'A cidade de {maior_indice_cidade} possui o maior indice de acidente de transito com {maior_indice_acidentes} acidentes.')
print(f'A cidade de {menor_indice_cidade} possui o menor indice de acidente de transito com {menor_indice_acidentes} acidentes.')
print(f'A media de veiculos nas 5 cidades é de {int(media_veiculos)} veiculos.')
print(f'A media de acidentes em uma cidade com menos 2000 veiculos é de  {int(media_acidentes)} acidentes.')
print('-' * 90)
