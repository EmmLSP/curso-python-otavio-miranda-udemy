# while e break - Estrutura de repetição (Parte 2) 

"""
Repetições 
While (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
break -> dentro de um laco procura o laco mais proximo
para interromper
"""

"""
while False:
    Code is not analyzed because condition is 
    statically evaluated as false Pylance
    print('EITA')

print('Acabou')
"""

contador = 0

print('Contador antes de print()')
print('0 = 0 + 1')
print('1 = 0 + 1')
print('print(1)')
while contador < 10:
    contador = contador + 1
    print(contador)
print(f'Valor depois do while: {contador}')

print()

contador = 0

print('Contador depois de print()')
print('0 = 0 + 1')
print('print(0)')
print('1 = 0 + 1')
while contador < 10:
    print(contador)
    contador = contador + 1
print(f'Valor depois do while: {contador}')

print()

contador = 0

print('Contar de 1 ate 11')
while contador <= 10:
    contador = contador + 1
    print(contador)

print('Acabou')

print()

contador = 0

print('Contar de 0 ate 10')
while contador <= 10:
    print(contador)
    contador = contador + 1

print('Acabou')
