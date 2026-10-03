#Faça um programa que leia um número de 0 a 9999 e mostre
#e mostre na tela cada um de seus dígitos separados
       #Ex: Digite uma número: 1834
       #unidade:4
       #dezena:3
       #centena:8
       #milhar:1
numero = input('Digite um numero de 0 a 9999: ')
print('Unidade: ', numero[3:])
print('Dezena: ', numero[2:3])
print('Centena: ', numero[1:2])
print('Milhar: ', numero[:1])









