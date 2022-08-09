print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if abs(s2-s3)<s1<(s2+s3) or abs(s1-s3)<s2<(s1+s3) or abs(s1-s2)<s3<(s1+s2):
    if s1 != s2 and s2 != s3 and s1 != s3:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo ESCALENO!')
    elif s1 == s2 and s2 == s3 and s1 == s3:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo EQUILÁTERO!')
    else:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')
