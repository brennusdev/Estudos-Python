print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} x'.format(termo), end='')
        termo = termo + razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar? : '))
print('Progressão finalizada com {] termo mostrados'.format(total))