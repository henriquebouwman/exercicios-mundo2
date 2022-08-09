n = int(input('Digite um número inteiro qualquer: '))
base = int(input('Qual será a base de conversão?\n 1 - BINÁRIO\n 2 - OCTAL\n 3 - HEXADECIMAL\n--->'))
if base == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif base == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif base == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('\033[31mCOMANDO INVÁLIDO!')


