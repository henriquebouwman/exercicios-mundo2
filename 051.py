print('=='*15)
print('10 TERMOS DE UMA P.A')
print('=='*15)
pr = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = pr + (11 - 1) * r
for i in range(pr, d , r):
    print('{} '.format(i), end='-> ')
print('ACABOU')