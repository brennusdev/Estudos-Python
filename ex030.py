número = int(input('Me diga um número qualquer : '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(resultado))
else:
    print('O número {} é IMPAR'.format(resultado))