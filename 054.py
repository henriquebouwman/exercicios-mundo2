from datetime import date
cont = 0
atual = date.today().year
for i in range(1, 8):
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    if idade >= 21:
        cont += 1
print('{} pessoas atigiram a maioridade e {} são menores.'.format(cont, 7 - cont))
