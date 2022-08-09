print('{:=^40}'.format(' LOJA X '))
preço = float(input('Preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final.'.format(preço, preço - (preço*(10/100))))
elif opção == 2:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final.'.format(preço, preço - (preço * (5/100))))
elif opção == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(preço/2))
    print('Sua compra de R$ {} vai custar R$ {:.2f} no final.'.format(preço, preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    preçojuros = preço + (preço* (20/100))
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(parcelas, preçojuros/parcelas))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, preçojuros))
else:
    print('OPÇÃO INVÁLIDA!')
    

