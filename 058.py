'''from random import randint
soma = 1
computador = randint(0, 11)
print('Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?
')
jogador = int(input('Qual é seu palpite?'))
while jogador != computador:
    soma += 1
    if jogador > computador:
        print('Menos... Tente mais uma vez.')
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    jogador = int(input('Qual é seu palpite?'))
print('Acertou com {} tentativas. Parabéns!'.format(soma))'''
from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue advinhar qual foi?
''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
           print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))


