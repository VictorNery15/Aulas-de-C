from random import randint
from time import sleep
print('~°'*38)
print('VAMOS JOGAR UM JOGO!!! Vou pensar em um numero de 1 a 5. tente adivinhar =D')
print('~°'*38)
a=int(input('Em qual numero eu pensei? '))
print('PROCESSADO...')
sleep(1.5)
b=(randint(1,5))
if b == a:
    print('PARABÉNS!! Você acertou!')
else:
    print(f'Você errou. O numero certo é o {b}')