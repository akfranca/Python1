#Escreva um programa que faça o computador "pensar"
#em um número inteiro entre 0 e 5 e peça para o
#usuário tentar descobrir qual foi o número escolhido pelo computador.
       #O programa deverá escrever na tela se o usuário
       #venceu ou perdeu.

import random
from time import sleep
import emoji
num = random.randint(0,5)
print(emoji.emojize('Vou pensar em um número :thinking_face:'))
pergunta = int(input('Em qual numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if pergunta == num:
    print(emoji.emojize('PARABÉNS :exploding_head:! Eu escolhi o número: {}'.format(num)))
else:
    print(emoji.emojize('QUE PENA :face_with_diagonal_mouth:! Não foi dessa vez! Eu escolhi o número {}.'.format(num)))

