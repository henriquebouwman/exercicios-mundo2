n = int(input('Digite um número [999 para parar]: '))
soma = 0
c = 0
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(c, soma))
