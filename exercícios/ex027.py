#Faça um programa que leia o nome completo
#de uma pessoa, mostrando em seguida o primeiro
#e o último nome separadamente.
      #Ex: Ana Maria de Souza
      #primeiro = Maria
      #último = Souza

nome = input('Digite seu nome completo: ').strip()
primeiro = nome.split()[0]
ultimo = nome.split()[-1]
print('Primeiro: {}'.format(primeiro))
print('Último: {}'.format(ultimo))


