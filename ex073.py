times = ( 'Atlético-MG', 'Athletico-PR','Bahia','Botafogo','Bragantino',
          'Chapecoense','Corinthians','Coritiba','Cruzeiro',
          'Flamengo','Fluminense','Grêmio','Internacional',
          'Mirassol','Palmeiras','Remo','Santos',
          'São Paulo','Vasco da Gama','Vitória')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos colocados: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense")} posição')
