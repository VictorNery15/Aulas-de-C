#
bn = int(input("\nDigite um numero em binario de 8 digitos: "))
un1 = bn // 1 % 10
un2 = bn // 10 % 10
un3 = bn // 100 % 10
un4 = bn // 1000 % 10
un5 = bn // 10000 % 10
un6 = bn // 100000 % 10
un7 = bn // 1000000 % 10
un8 = bn // 10000000 % 10
sm = 0

if un8 == 1:
    sm += 128

if un7 == 1:
    sm += 64

if un6 == 1:
    sm += 32

if un5 == 1:
    sm += 16

if un4 == 1:
    sm += 8

if un3 == 1:
    sm += 4

if un2 == 1:
    sm += 2

if un1 == 1:
    sm += 1

print('\nO numero binario:')
print(f'\n{un8} | {un7} | {un6} | {un5} | {un4} | {un3} | {un2} | {un1}\n')
print(f'Equivale a {sm} em decimal.\n')