
num=int(input('Digite um numero de 1 a 9999: '))
u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m=num // 1000 % 10
print(f'Unidadde: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')


'''
n=str(input('Digite um numero inteiro de 1 a 9999: ')).strip()
if not(n.isnumeric()):
    print('Nada disso >=C')
if(n.isnumeric()):
    if(len(n)==1):
        print(f'Unidade: {n}\nDezena: 0\nCentena: 0\nMilhar: 0')
    if(len(n)==2):
        print(f'Unidade: {n[1]}\nDezena: {n[0]}\nCentena: 0\nMilhar: 0')
    if(len(n)==3):
        print(f'Unidade: {n[2]}\nDezena: {n[1]}\nCentena: {n[0]}\nMilhar: 0')
    if(len(n)==4):
        print(f'Unidade: {n[3]}\nDezena: {n[2]}\nCentena: {n[1]}\nMilhar: {n[0]}')
    if(len(n)>4):
        print('Meu fi é de 1 a 9999 >=c')
'''