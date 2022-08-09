print('--'*20)
print('{:^40}'.format('LOJÃO SUPER BARATÃO'))
print('--'*20)
total = prodmil = cont = menor = 0
nomebarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        prodmil += 1
    if cont == 1:
        menor = preço
        nomebarato = nome
    else:
        if preço < menor:
            menor = preço
            nomebarato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Temos {prodmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R$ {menor}')

