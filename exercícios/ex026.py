#Faça um programa que leia uma frase
#pelo teclado e mostre:
  #Quantas vezes aparece a letra "a"
  #Em que posição ela aparece a primeira vez
  #Em que posição ela aparece última vez

frase = input('Digite uma frase: ').lower().strip()
a = frase.count('a')
b = frase.find('a') +1
c = frase.rfind('a') +1
print('A frase contém {} vezes a letra a'.format(a))
print('Primeira posição da letra a {}'.format(b))
print('Última posição da letra a {}'.format(c))


