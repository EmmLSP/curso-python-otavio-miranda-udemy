# Introdução ao for / in - estrutura de repetição para coisas finitas

# usa o while quando nao se sabe a quantidade de repeticoes
# que serao necessarias para encerrar o laco

senha_salva = '123456' # senha salva no banco de dados
senha_digitada = ''
repeticoes = 0
limite = 5

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
    repeticoes += 1

print(repeticoes)
print('Aquele laco acima pode ter repeticoes infinitas')

# for usado quando se sabe a quantidade de vezes que um
# laco vai acontencer
# a string é interavel, passando em uma string 
# um valor por vez -> 'Python' -> 6 caracteres

texto = 'Python'

for letra in texto:
    print(letra)
print()

for i in range(0, len(texto)):
    print(texto[i])
print()

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'

print(novo_texto + '*')
