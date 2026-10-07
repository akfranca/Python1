#Faça um programa que leia um ano qualquer
#e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} É BISSEXTO!'.format(ano))
        else:
            print('O ano {} NÃO é BISSEXTO!'.format(ano))
    else:
        print('O ano {} É BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))

#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
  #quer dizer que: se o ano é divisil por 4 sobra 0 é divisivel por 100 e sobra algo e é divisivel ou divisilvel por 400 sobra 0

#para pegar o ano atual você deve importar date
#from datetime import date
#data.today().year








