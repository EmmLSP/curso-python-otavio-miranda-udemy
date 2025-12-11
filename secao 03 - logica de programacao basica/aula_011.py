# Precedencia entre os operadores aritmeticos

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# parentese internos sempre sao executados primeiro
# comecando do mais interno ate o mais externo

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)
conta_2 = (1 + 1) ** (5 + 5) # 1024
print(conta_2)
conta_3 = (1 + (0.5 + 0.5)) ** 5 + 5
print(conta_3)
conta_4 = int(1 + (0.5 + 0.5)) ** 5 + 5
print(conta_4)
conta_5 = (1 + int(0.5 + 0.5)) ** 5 + 5
print(conta_5)
