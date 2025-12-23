"""
Exercicio 003
Faca um programa que leia e valide as seguintes
informações:
- Nome: maior que 3 caracteres
- Idade: entre 0 e 150
- Salario: maior que zero
- Sexo: 'f' ou 'm'
- Estado Civil: 's', 'c', 'v' e 'd'
"""

while True:
    nome = input('Digite seu nome: ')
    if len(nome) >= 3:
        break
    print('Nome precisa ter mais de 3 caracteres')

while True:
    idade = input('Digite sua idade: ')
    try:
        idade_int = int(idade)
        if 0 <= idade_int <= 150:
            break
        print('idade precisa ser entre 0 e 150')
    except:
        print('Idade precisa ser um numero inteiro')

valida_dados = False
while not valida_dados:
    salario = input('Digite seu salario: R$ ')
    try:
        salario_float = float(salario)
        if salario_float > 0:
            valida_dados = True
        else:
            print('Salario precisa ser maior que zero')
    except:
        print('Salario precisa ser um numero float')

valida_dados = False
while not valida_dados:
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo in 'MF':
        valida_dados = True
        if sexo == 'F':
            sexo = 'Feminino'
        else:
            sexo = 'Masculino'
    else:
        print('Sexo invalido! Digite \'f\' ou \'m\'')

while True:
    estado_civil = input('Digite seu estado civil (s, c, v ou d): ').lower()

    if estado_civil not in 'csvd':
        print('Estado civil invalido! Digite \'s\', \'c\', \'v\' ou \'d\'')
        continue
    if estado_civil == 's':
        estado_civil = 'Solteiro(a)'
    elif estado_civil == 'c':
        estado_civil = 'Casado(a)'
    elif estado_civil == 'v':
        estado_civil = 'Viuvo(a)'
    else:
        estado_civil = 'Divorciado(a)'
    break

print('-' * 30)
print(f'Nome.............: {nome}')
print(f'Idade............: {idade} anos')
print(f'Salario..........: R${salario_float:.2f}')
print(f'Sexo.............: {sexo}')
print(f'Estado civil.....: {estado_civil}')
print('-' * 30)
