#Crie um programa que leia um número inteiro
#e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print('Seu número escolhido é {} e ele é PAR'.format(numero))
else:
    print('Seu numero escolhido é {} e ele é ÍMPAR'.format(numero))



