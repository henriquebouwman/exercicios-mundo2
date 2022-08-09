nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))
if media >= 7:
    print('O aluno está \033[32mAPROVADO\033[m!')
elif media < 5:
    print('O aluno está \033[31mREPROVADO\033[m!')
else:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m!')