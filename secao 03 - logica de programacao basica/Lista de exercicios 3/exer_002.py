"""
Exercicio 002
Faca um programa que leia o nome de usuario e a senha
e nao aceite a senha igual ao nome do usuario mostrando
uma nesangem de erro e voltando a pedir informações.
"""

while True:
    usuario = input('Digite seu nome de usuario: ')
    senha = input('Digite sua senha: ')
    if usuario != senha:
        print('Entrada Válida!')
        break
    print('Erro: Usuario e senha iguais, digite novamente.')

print(f'Usuario: {usuario}')
print(f'Senha: {senha}')
