from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor:'))
opção = 0
somar = primeiro + segundo
mutiplicar = primeiro * segundo
while opção != 5:
    print('''\n    [1] SOMAR 
    [2] MUTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('\n>>>> Qual é sua opção? '))
    if opção == 1:
        print('\nA soma entre {} + {} é {}.'.format(primeiro, segundo, somar))
    elif opção == 2:
        print('\nO resultado de {} x {} é {}. '.format(primeiro, segundo, mutiplicar))
    elif opção == 3:
        if primeiro > segundo:
            print('\nEntre {} e {}, o maior valor é {}.'.format(primeiro, segundo, primeiro))
        elif primeiro < segundo:
            print('\nEntre {} e {}, o maior valor é {}.'.format(primeiro, segundo, segundo))
        else:
            print('\nOs valores {} e {} são iguais.'.format(primeiro, segundo))
    elif opção == 4:
        print('\nInforme os novos valores: ')
        primeiro = int(input('\nPrimeiro valor: '))
        segundo = int(input('Segundo valor:'))
    elif opção == 5:
        print('\nFinalizando...')
        sleep(2)
    else:
        print('\nOpção inválida, tente novamente.')
    sleep(1)
print('Fim do programa! Volte sempre!')

