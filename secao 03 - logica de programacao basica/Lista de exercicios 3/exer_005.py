"""
Exercicio 005
Altere o exercicio anterior permitindo ao usuario informar as
populacoes e as taxas de crescimento iniciais. Valide a entrada
e permita repetir a operacao.
"""

while True:
    pop_pais_a = float(input('Digite a poulacao do pais A: '))
    pop_pais_b = float(input('Digite a poulacao do pais B: '))
    if pop_pais_a > pop_pais_b:
        print('A populacao do pais A precisa ser menor do que ', end='')
        print('a populacao do pais B')
        continue
    break

valida_taxa = False
while not valida_taxa:
    taxa_pais_a = input('Digite a taxa de crescimento do pais A: ')
    taxa_pais_b = input('Digite a taxa de crescimento do pais B: ')

    try:
        taxa_pais_a = float(taxa_pais_a)
        taxa_pais_b = float(taxa_pais_b)

        if taxa_pais_a > taxa_pais_b:
            break
        
        print('A taxa de crescimento do pais A precisa ser menor do que ', end='')
        print('a taxa de crescimento do pais B')
    except:
        continue

anos = 0

while pop_pais_a <= pop_pais_b:
    pop_pais_a += (pop_pais_a * taxa_pais_a / 100)
    pop_pais_b += (pop_pais_b * taxa_pais_b / 100)
    anos += 1

print(f'Serao necessarios {anos} anos para a populacao ', end='')
print('do pais A ultrapassar a populacao do pais B')
