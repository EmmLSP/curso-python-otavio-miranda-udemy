# Fatiamento de strings e a função len

"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a funcao len() retorna a qtd
de caracteres da str
' ' -> espaco caractere que conta bytes -> bool 1
''  -> espaco vazio nao conta bytes -> bool 0
"""

print('-' * 28)
print(' 0  1  2  3  4  5  6  7  8')
print(' O  l  á     m  u  n  d  o')
print('-9 -8 -7 -6 -5 -4 -3 -2 -1')
print('-' * 28)

variavel = 'Olá mundo'

print(variavel[5]) # u
print(variavel[-4]) # u
print()

print(variavel[4:])
print(variavel[4:9])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2]) # lá mun
print()

print(variavel[0:9:1])
print(variavel[::-1]) # odnum álO -> inverter ordem
print(variavel[-1:-10:-1]) # odnum álO
print(variavel[::2]) # Oámno
print(variavel[:len(variavel):1]) # [0:9:1]
print(variavel[:len(variavel) - 1:1]) # [0:8:1]
print(variavel[:len(variavel):2]) # [0:8:2] -> Oámno
print()

# len()
print(len(variavel)) # 9 caracteres
print(len(variavel[3])) # 1
print(len(variavel[variavel.find(' ')])) # 1
print()

# count() 
print(variavel.count(' ')) # 1
print(variavel.count(variavel[3])) # 1
print(variavel.count(variavel[-6])) # 1
print(variavel.count(variavel[variavel.find(' ')])) # 1
print()
