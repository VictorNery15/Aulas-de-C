from datetime import date
ano = int(input('Digite o ano á ser analisado. Coloque 0 pra analisar o ano atual: '))
if ano == 0:
    ano=date.today().year
if ano%4 ==0 and ano%100 != 0 or ano%400 == 0:
    print(f'O ano de {ano} é um ano Bissexto.')
else:
    print(f'O ano de {ano} não é um ano Bissexto.')


'''a=int(input('Digite um ano para analisar: '))
if a%4 >= 1:
    print(f'O ano de {a} não é um ano bissexto.')
if a%100 == 0:
    if a%400 == 0:
        print(f'O ano de {a} é um ano bissexto.')
    else:
        print(f'O ano de {a} não é um ano bissexto.')
if a//1%10 >0:
    if a%4 == 0:
        print(f'O ano de {a} é um ano bissexto.')'''
