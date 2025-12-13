# if, elif e else: entendendo o fluxo do interpretador em condicionais

# if  / elif       / else
# se  / se nao se  / se nao

# ... ellipsys - deixar para escrever depois
# pass - passa codigo, pula

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Codigo para a condicao 1')
elif condicao2:
    print('Codigo para a condicao 2')
elif condicao3:
    print('Codigo para a condicao 3')
elif condicao4:
    print('Codigo para a condicao 4')
else:
    print('Nenhuma condicao foi satisfeita')

if 10 == 10:
    print('Outro if')

print('Fora do if')
