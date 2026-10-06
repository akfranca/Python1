#Escreva um programa que leia a velocidade de um carro
     #se ele ultrapassar 80km/h, mostre uma
     #mensagem dizendo que foi multado.
#A multa vai custar R$7,00 por cada km acima do limite

velocidade = float(input('Digite sua velocidade: '))
multa = (velocidade - 80) * 7.0
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80Km/h')
    print('Sua multa é de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')

