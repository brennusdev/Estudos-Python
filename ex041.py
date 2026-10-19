from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9 :
    print('Classificação: MIRIM')
elif idade <= 14 :
   print('Classificação: INFANTIL')
elif idade <= 19 :
    print('Classificação: Júnior')
elif idade <= 25 :
    print('Classificação: Sênior')
elif idade <= 30 :
    print('Classificação: Master')