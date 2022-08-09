'''from time import sleep
print('Gerador de PA')
print('-='*10)
termo = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
for i in range(10):
    print('{} -> '.format(termo), end='')
    termo += r
print('PAUSA')
c = 10
while True:
    variavel = int(input('Quantos termos você quer mostrar a mais?'))
    if variavel == 0:
        sleep(1)
        print('Finalizando...')
        break
    for i in range(variavel):
        print('{} -> '.format(termo), end='')
        termo += r
    c += variavel
    print('PAUSA')
print('Progressão finalizada com {} termos mostrados.'.format(c))'''
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = primeiro
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSE')
    mais = int (input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))




