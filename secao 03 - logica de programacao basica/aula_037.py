# while + continue - pulando alguma repetição

"""
Repetiões
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> quando um codigo nao tem fim
break -> termina o laco imediatamente
continue -> pular um loop
break e continue sao usadas para o while que estiver mais proximo
"""

contador = 0

print('break -> quebra o laco -> imprime de 1 ate 4')
while contador <= 10:
    contador += 1
    print(contador)
    if contador == 4:
        break

print('Acabou\n')

contador = 0

print('continue -> pular o 6 com continue e parar no 40 com break')
while contador < 100:
    contador += 1

    # pular o numero 6 do contador 
    if contador == 6:
        print('Pulando o 6')
        print('Não vou mostrar o', contador)
        continue

    if contador == 10:
        print(f'Pulando do 10 ate 27')

    # pular do 10 ate 27
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    # if contador == 40:
    #    continue -> esta anulando a funcao do break
    #    break Code is structurally unreachable

    # vai parar no numero 40 do contador
    if contador == 40:
        break

print('Acabou')
