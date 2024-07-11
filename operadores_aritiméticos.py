# Ordem de Precedencia
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

n1 = int(input('Valor 1:'))
n2 = int(input('Valor 2:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
print('A soma é: {}, a multiplicação é: {} a divisão é: {} e a esponencial é: {}'.format(s,m,d,e))

# format foi utilizado no final para nomear todos os {}. um por um separados por vígula.