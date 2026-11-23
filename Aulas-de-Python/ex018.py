from math import sin, cos, tan, radians

x=float(input('Digite um angulo:'))
a=radians(x)
s=sin(a)
c=cos(a)
t=tan(a)
print(f'O angulo tem:\nSeno de {s:.2f}\nCosseno de {c:.2f}\nTangente de {t:.2f}')