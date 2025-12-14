# Flags, is, is not e None

"""
O que algoritmo na programacao

Um algoritmo, na programação, é uma sequência lógica e ordenada de 
passos usada para resolver um problema ou executar uma tarefa.

Em outras palavras:
é a receita que o computador segue para chegar a um resultado.

Definição simples
Algoritmo = passos bem definidos + ordem correta + objetivo claro

Características de um bom algoritmo
✔ Claro e fácil de entender
✔ Tem começo, meio e fim
✔ Resolve um problema específico
✔ Pode ser transformado em código (Java, Python, C, etc.)
"""

"""
Flag (Bandeira) - Marcar um local
None - nao valor
is e is not = é ou nao é (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Não faca algo')

# print(passou_no_if, passou_no_if is None) -> False
# print(passou_no_if, passou_no_if is not None) -> True

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
