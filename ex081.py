valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em  ordem decrescente são {valores}')
if 5 in valores:
    print(' O VALOR 5 foi digitado na lista')
else:
    print('O valor 5 não foi encontrado na lista')