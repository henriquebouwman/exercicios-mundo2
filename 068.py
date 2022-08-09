from time import sleep
# fazer um loop onde caso ganhe continue
'''variavel = ''
cont = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
while True:
    computador = randint(0,10)
    jogador = int(input('Diga um valor: '))
    opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = jogador + computador
    if soma % 2 == 0:
        variavel = 'PAR'
    else:
        variavel = 'ÍMPAR'
    print('VAMOS')
    sleep(0.5)
    print('ARRAS...')
    sleep(0.75)
    print('TAR!!')
    print('--' * 15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {variavel}.')
    print('--'*15)
    if opção in variavel[0]:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-' * 15)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            v += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            v += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=-' * 15)
print(f'GAME OVER! Você venceu {v} vezes.')




