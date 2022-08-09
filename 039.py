from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano

if idade > 18:
    print('Você tem {} anos e \033[33mJÁ PASSOU\033[m do tempo de se alistar.'.format(idade))
    print('Seu alistamento era pra ter sido feito em {}.'.format(ano+18))
elif idade < 18:
    print('Você tem {} anos e \033[31mAINDA NÃO ESTÁ\033[m na hora de se alistar.'.format(idade))
    print('Você terá que se alistar em {}.'.format(ano+18))
else:
    print('Você tem 18 anos e \033[32mESTÁ EXATAMENTE\033[m na hora de se alistar.')