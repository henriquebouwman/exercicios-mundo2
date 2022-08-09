while True:
    print('-'*40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for i in range(11):
        print(f'{n} x {i} = {n * i}')
