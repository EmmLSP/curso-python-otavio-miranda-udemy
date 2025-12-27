"""
Exercicio 011
Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre:

- A media de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 21 anos
"""

soma_idades = qtd_homens = qtd_mulheres = 0
homem_mais_velho = mulher_menor = ''
homem_idade_maior = mulher_idade_menor = mulheres_menores = 0
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    
    valida_dados = False
    while not valida_dados:
        nome = input('Nome: ').strip()
        if len(nome) < 3:
            print('Nome precisa de pelos menos 3 caracteres')
            continue
        break

    valida_dados = False
    while not valida_dados:
        idade = int(input('Idade: '))
        if idade <= 0:
            print('Idade precisa ser maior que zero')
            continue
        break  

    valida_dados = False
    while not valida_dados:
        sexo = input('Sexo [M/F]: ').upper().strip()
        if sexo not in 'MF':
            print('Sexo invalido! Digite \'M\' ou \'F\'')
            continue
        break
    soma_idades += idade

    if sexo == 'M':
        if idade > homem_idade_maior:
            homem_idade_maior = idade
            homem_mais_velho = nome
        qtd_homens += 1

    if sexo == 'F':
        qtd_mulheres += 1

    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
        if mulheres_menores == 1:
            mulher_idade_menor = idade
            mulher_menor = nome
        else:
            if idade < mulher_idade_menor:
                mulher_idade_menor = idade
                mulher_menor = nome

media_idade = soma_idades / 4

print('-' * 50)
print(f'A media de idade do grupo é de {media_idade:.1f} anos')
if qtd_homens == 0:
    print('Não tem nenhum homem no grupo')
else:
    print(f'No grupo ha {qtd_homens} homens ao todo')
    print(f'O homem mais velho tem {homem_idade_maior} anos e se chama {homem_mais_velho}')
if qtd_mulheres == 0:
    print('Nao tem nenhuma mulher no grupo')
else:
    print(f'No grupo ha {qtd_mulheres} mulheres ao todo')
    if mulheres_menores == 0:
        print('Nao tem nenhuma mulher com menos de 20 anos')
    else:
        print(f'Ao todo sao {mulheres_menores} mulheres com menos de 20 anos')
        print(f'A mulher mais nova tem {mulher_idade_menor} anos e se chama {mulher_menor}')
