maiores = mulheres20 = homens = 0
while True:
    print('--' * 15)
    print('CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Idade: '))
    if idade >= 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    continuar = ' ' 
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')




