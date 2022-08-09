print('--'*15)
print('Sequência de Fibonacci')
print('--'*15)
t = int(input('Quantos termos você quer mostrar?'))
n1 = 0
n2 = 1
print('~'*30)
print('{} -> {}'.format(n1, n2),end='')
c = 3
while c <= t:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    c += 1
print(' -> FIM')
print('~'*30)


