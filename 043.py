peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (M)'))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc < 24.9:
    print('Você está no PESO NORMAL.')
elif imc < 29.9:
    print('Você está SOBREPESO.')
elif imc < 34.9:
    print('Você está na OBESIDADE GRAU I.')
elif imc < 39.9:
    print('Você está na OBESIDADE GRAU II.')
else:
    print('Você está na OBESIDADE GRAU III OU MÓRBIDA.')