soma = 0
cont = 0
for i in range(1,7):
    n = int(input('Digite o {} valor: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você informou {} número(s) par(es) e a soma dele(s) foi {}.'.format(cont, soma))
