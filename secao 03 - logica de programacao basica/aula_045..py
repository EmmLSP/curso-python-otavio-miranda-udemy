# Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

"""
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)
print()

texto = 'Luiz'.__iter__()
print(texto)

texto = iter('Luiz') # __iter__()
print(texto)
print()

texto = 'Luiz' #    __iter__()
texto = iter('Luiz')
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
# print(texto.__next__()) -> erro -> StopIteration
print()

texto = iter('Luiz') # __iter__()
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
# print(next(texto)) -> erro -> StopIteration
print()

# erro: StopIteration -> Python pedindo para parar iteracao
# tratar o erro quando se esgota as iteracoes

# tratar o erro StopIteration com try except dentro 
# de um while True, quando encntrar o erro da um break

texto = 'Gustavo' # iteravel
iterador = iter(texto) # iterator

# Tratando o erro StopIteration com try except
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
print()

texto = 'Luiz'
for letra in texto:
    print(letra)
