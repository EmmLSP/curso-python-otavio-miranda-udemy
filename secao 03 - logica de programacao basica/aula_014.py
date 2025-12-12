# Formatacao de strings com o metodo format

# argumento: a, b, c
# parametro nomeado: nome3
# tudo que vier depois de uma parametro 
# nomeado tambem precisa ser nomeado
# chaves nomeados: {0}, {1}, {nome3}

# em Python tudo e um objeto
# string é um objeto da classe String
# usando um metodo, funcao -> format()
# quando uma funcao esta dentro de um 
# objeto ela e chamada de metodo

a = 'AAA'
b = 'BBB'
c = 1.1

# string = 'a={0} b={1} b={1} a={0} c={2:.2f}' 
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' 
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)
