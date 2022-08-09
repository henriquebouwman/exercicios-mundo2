vcasa = float(input('Qual o valor da casa? R$'))
vsalario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos vai pagar? '))
meses = anos * 12
parcela = vcasa/meses
if parcela <= vsalario * (30 / 100):
    print('O empréstimo foi \033[32mAPROVADO\033[m! O valor da prestação mensal é de R${:.2f}.'.format(parcela))
else:
    print('O empréstimo foi \033[31mNEGADO\033[m!')
