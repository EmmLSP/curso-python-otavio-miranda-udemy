"""
Exercicio 008
Crie um programa que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espacos.

Ex: 
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""

# v1
palindromo = []
frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)

for c in range(len(junto)):
    palindromo.append(junto[c])

for c in range(len(junto) // 2):
    temp = palindromo[c]
    palindromo[c] = palindromo[len(junto) - 1 - c]
    palindromo[len(junto) - 1 - c] = temp
palindromo = ''.join(palindromo)
print(f'O inverso de {junto} é {palindromo}')
if junto == palindromo:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada não é um PALINDROMO!')
print()

# v2
frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)

palindromo = ''
for c in range(len(junto)):
    palindromo += junto[len(junto) - 1 - c]
print(f'O inverso de {junto} é {palindromo}')
if junto == palindromo:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada não é um PALINDROMO!')
print()

# v3
frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)

palindromo = ''
for c in range(len(junto) - 1, -1, -1):
    palindromo += junto[c]
print(f'O inverso de {junto} é {palindromo}')
if junto == palindromo:
    print('Temos um PALINDROMO!')
else:
    print('A frase digitada não é um PALINDROMO!')
