frase = str(input('Digite uma palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''