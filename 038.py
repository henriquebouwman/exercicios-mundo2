n1 = int(input('\033[34mPrimeiro número: '))
n2 = int(input('\033[33mSegundo número:\033[m '))
if n1 > n2:
    print('O \033[34mPRIMEIRO\033[m VALOR ({}) é o MAIOR.'.format(n1))
elif n2 > n1:
    print('O \033[33mSEGUNDO\033[m VALOR ({}) é o MAIOR.'.format(n2))
else:
    print('Os números são IGUAIS.')

