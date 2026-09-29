from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = sqrt (co**2 + ca**2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
