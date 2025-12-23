"""
Exercicio 004
Supondo a populacao de um pais A seja da ordem de 80000 
habitantes com uma taxa de crescimento de 3% e que a 
populacao de B seja 200000 habitantes com uma taxa de 
crescimento de 1.5%. Faca um programa que calcule e 
escreva o numero de anos necessarios para que a populacao 
do pais A ultrapasse ou iguale a  populacao do pais B, 
mantida as taxas de crescimento.
"""

pop_pais_a = 80000
pop_pais_b = 200000

taxa_pais_a = 3
taxa_pais_b = 1.5

anos = 0

while pop_pais_a <= pop_pais_b:
    pop_pais_a += (pop_pais_a * taxa_pais_a / 100)
    pop_pais_b += (pop_pais_b * taxa_pais_b / 100)
    print(f'Populacao pais A = {pop_pais_a:.2f}', end='')
    print(f' - Populacao pais B = {pop_pais_b:.2f}')
    anos += 1

print(f'Serao necessarios {anos} anos para a populacao ', end='')
print('do pais A ultrapassar a populacao do pais B')
