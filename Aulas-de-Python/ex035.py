
print('~-'*20)
print('Analisador de Triângulos')
print('~-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('Os segmentos acima PODEM FORMA triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMA triângulo!')

'''
a = float(input('Digite o valor de uma reta: '))
b = float(input('Digite outra reta: '))
c = float(input('Digite mais uma: '))
if a == b == c:
    print('Essas retas podem fazer um triângulo.')
else:
    if a >= b and a >= c:
        if b + c > a:
            print('Essas retas podem fazer um triângulo.')
        else:
            print('Esssas retas não podem fazer um triângulo.')
    if b >= a and b >= c:
        if a + c > b:
            print('Essas retas podem fazer um triângulo.')
        else:
            print('Essas retas não podem fazer um triângulo.')
    if c >= b and c >= a:
        if a + b > c:
            print('Essas retas podem fazer um triângulo.')
        else:
            print('Essas retas não podem fazer um triângulo.')
'''