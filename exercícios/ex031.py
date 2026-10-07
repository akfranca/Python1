#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passage, cobrando R$0,50 por Km para viagens até 200Km
#e R$0,45 para viagens mais longas.

km = float(input('Qual a distância de sua viagem? '))
if km <= 200:
    passagem_cara = km * 0.50
    print('O custo da sua passagem é de R${:.2f}'.format(passagem_cara))
else:
    passagem_barata = km * 0.45
    print('O custo da sua passagem é de R${:.2f}'.format(passagem_barata))
print('BOA VIAGEM!')

