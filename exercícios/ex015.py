km = float(input('Quantos km rodados? '))
d = int(input('Quantos dias alugado? '))
v = (km * 0.15) + (d * 60.00)
print('O total a pagar é de R$ {:.2f}'.format(v))

