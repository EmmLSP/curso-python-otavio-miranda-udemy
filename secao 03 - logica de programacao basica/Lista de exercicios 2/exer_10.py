"""
Exercicio 10
Faca um programa que pergunte em que turno voce estuda. Peca 
para digitar M-Matutino, V-Vespertino e N-Noturno. Imprima a 
mensagem "Bom Dia!", "Boa Tarde!" e "Boa Noite!" ou "Valor
invalido!", conforme o caso.
"""
print("""---------------
M - Matutino
V - Vespertino
N - Noturno
---------------""")
turno = input('Digite qual turno voce estuda: ').upper().strip()
tam = len(turno)
if turno.isalpha():
    if tam == 1:
        if turno == 'M':
            print('Bom Dia!')
        elif turno == 'V':
            print('Boa Tarde!')
        elif turno == 'N':
            print('Boa Noite!')
        else:
            print('Valor invalido!')
    else:
        print('Não e uma letra')
else:
    print('Não é alfabetico')
