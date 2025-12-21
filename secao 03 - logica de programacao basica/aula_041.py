# while / else (recurso peculiar do Python)

# else e executado quando o laco vai ate o final
# break -> interrompe o laco e o else nao e executado

string = 'Valor qualquer' 

i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('O else foi executado')
print('Fora do while')

string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Nao encontrei um espaco na string')
print('Fora do while')
