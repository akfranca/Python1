# Crie um programa que leia o nome completo de uma pessoa e mostre:
             #nome com todas as letras maiúsculas
             #nome com todas as letras minúsculas
             #quantas letras tem sem considerar espaços
             #quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
print(len(nome.split()[0]))





