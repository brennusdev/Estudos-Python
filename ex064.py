núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um número [999 para parar]: '))
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('VocÊ digitou {} números e a soma entre eles foi {}'.format(cont, soma))