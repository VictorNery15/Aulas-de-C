salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 /100)
print(f'Quem ganhava R${salário:.2f} passa a ganhar R${novo:.2f} agora')


'''s = float(input('Digite o valor do seu salário atual: R$'))
if s >= 1250:
    print(f'Seu salário aumento de R${s} para R${s*0.1+s:.2f}')
else:
    print(f'Seu salário aumento de R${s} para R${s*0.15+s:.2f}')'''