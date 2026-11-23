from math import sqrt,hypot
'''c1=float(input('Digite o valor do cateto oposto:'))
c2=float(input('Agora o cateto adjacente:'))
h=(c1**2+c2**2)**0.5
print(f'A hipotenusa vai medir {h:.2f}')'''

'''c1=float(input('Digite o valor do cateto oposto:'))
c2=float(input('Agora o cateto adjacente:'))
h=sqrt(c2**2+c1**2)
print(f'A hipotenusa vai medir {h:.2f}')'''

c1=float(input('Digite o valor do cateto oposto:'))
c2=float(input('Agora o cateto adjacente:'))
h=hypot(c1,c2)
print(f'A hipotenusa vai medir {h:.2f} ')
