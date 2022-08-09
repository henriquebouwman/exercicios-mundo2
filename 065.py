resp = 'S'
quant = media = soma = maior = menor = 0
while resp == 'S':
    quant += 1
    n = int(input('Digite um número: '))
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = soma/quant
print('Você digitou {} números e a média foi {:.2f}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
