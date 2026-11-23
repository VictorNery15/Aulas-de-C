print('Bem vindo a nossa comninhia de viagens!!')
d=float(input('Por favor digite a distancia da sua viagem. Km:'))
if d <= 200:
    print(f'DISTANCIA: {d} Km\nVALOR: R${d*0.5:.2f}')
else:
    print(f'DISTANCIA: {d} Km\nValor: R${d*0.45:.2f}')

#v= d * 0.50 if d <= 200 else d * 0.45