#Desafio 38
n1 = float(input('Give me a number: '))
n2 = float(input('Other number now: '))
if n1 > n2:
    print(f'-'*60,"\nThe first number is greater than the second")
    print('-'*60)
elif n2 > n1:
    print(f'-'*60,"\nThe second number is greater than the first")
    print(60*'-')
else:
    print(f'-'*60,"\nThe two number have the same value, because it's the same.")
    print(60*'-')