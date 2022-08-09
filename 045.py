import time
import random
print('''Suas opções são:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
escolha = int(input('Qual é sua jogada? '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.75)
print('PO!!!')
time.sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)
print('-='*12)
print('Computador jogou {}.'.format(computador))
if escolha == 1:
    print('Jogador jogou PEDRA.')
elif escolha == 2:
    print('Jogador jogou PAPEL')
elif escolha == 3:
    print('Jogador jogou TESOURA')
else:
    print('Jogador jogou INVÁLIDO')
print('-='*12)
if escolha == 1 and computador == 'TESOURA' or escolha == 2 and computador == 'PEDRA' or escolha == 3 and computador == 'PAPEL':
    print('JOGADOR VENCE')
elif computador == 'PEDRA' and escolha == 3 or computador == 'PAPEL' and escolha == 1 or computador == 'TESOURA' and escolha == 2:
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
