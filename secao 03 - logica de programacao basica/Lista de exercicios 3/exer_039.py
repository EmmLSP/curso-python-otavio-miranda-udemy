"""
Exercicio 039
Faca um programa que leia dez conjuntos de dois
valores, o primeiro representando o numero do 
aluno e o segundo representando a sua altura em
centimetros. Encontre o aluno mais alto e o mais
baixo. Mostre o numero do aluno mais alto e o
numero do aluno mais baixo, junto com suas 
alturas.
"""

mais_alto = mais_baixo = 0
num_alto = num_baixo = aluno_alto = aluno_baixo = 0
for aluno in range(1, 10+1): 
    while True:
        numero_aluno = int(input(f'Digite o numero do aluno {aluno}: # '))
        if numero_aluno < 0:
            print('Numero deve ser maior que zero')
            continue
        if len(str(numero_aluno)) < 4:
            print('Numero do aluno deve ter 4 digitos')
            continue
        break
    
    while True:
        altura_aluno = int(input(f'Digite a altura do aluno {aluno}: cm '))
        if altura_aluno < 0:
            print('Altura deve ser maior que zero')
            continue
        if  altura_aluno < 100 or altura_aluno > 210:
            print('Altura deve ser entre 100cm e 210cm')
            continue
        break
    
    if aluno == 1:
        mais_alto = mais_baixo = altura_aluno
        num_alto = num_baixo = numero_aluno
        aluno_alto = aluno_baixo = aluno
    else:
        if altura_aluno > mais_alto:
            mais_alto = altura_aluno
            num_alto = numero_aluno
            aluno_alto = aluno
        if altura_aluno < mais_baixo:
            mais_baixo = altura_aluno
            num_baixo = numero_aluno
            aluno_baixo = aluno

print(f'O aluno {aluno_alto} é o mais alto, codigo {num_alto} com {mais_alto} cm')
print(f'O aluno {aluno_baixo} é o mais baixo, codigo {num_baixo} com {mais_baixo} cm')
