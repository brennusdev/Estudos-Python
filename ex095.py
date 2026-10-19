time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clean()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy() )
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
        if resp in 'N':
            break
    print('-=' * 30)
    print('cod', end=' ')
    for i in  jogador.keys():
        print(f'{i:<15} ', end='')
    print()
    print('-=' * 40)
    print('<< VOLTE SEMPRE!>>')