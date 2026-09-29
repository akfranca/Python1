from math import cos, sin, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
radiano = radians(angulo)
cosseno = cos(radiano)
seno = sin(radiano)
tangente = tan(radiano)
print('O valor do cosseno é {:.4f}'.format(cosseno))
print('O valor do seno é {:.4f}'.format(seno))
print('O valor da tangente é {:.1f}'.format(tangente))


