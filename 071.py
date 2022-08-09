print('=='*20)
print('{:^40}'.format('BANCO HVB'))
print('=='*20)
valor = float(input('Que valor você quer sacar?'))
notas_50 = valor // 50
if notas_50 != 0:
    print(f'Total de {notas_50:.0f} cédulas de R$50')
notas_20 = (valor - (notas_50 * 50)) // 20
if notas_20 != 0:
    print(f'Total de {notas_20:.0f} de R$20')
soma1 = (notas_50 * 50) + (notas_20 * 20)
notas_10 = (valor - soma1) // 10
if notas_10 != 0:
    print(f'Total de {notas_10:.0f} de R$10')
soma2 = soma1 + (notas_10 * 10)
notas_1 = (valor - soma2) // 1
if notas_1 != 0:
    print(f'Total de {notas_1:.0f} de R$1')
print('=='*20)
print('Volte sempre ao BANCO HVB! Tenha um bom dia!')
