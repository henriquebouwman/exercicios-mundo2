maior = 0
soma = 0
mulheres20 = 0
media = 0
nomevelho = ''
for p in range(1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()
    soma += idade
    if p == 1 and sexo == 'M':
        maior = idade
        nomevelho = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
media = soma / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres20))

