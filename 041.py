from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Júnior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')
