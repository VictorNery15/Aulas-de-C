#Codigo da aula
a=int(input('Primeiro valor:'))
b=int(input('Segundo valor: '))
c=int(input('Terceiro valor: '))
#Verificando quem é menor
menor=a
if b<=a and b<=c:
    menor=b
if c<=a and c<=b:
    menor=c
#Verificando quem é maior
maior=a
if b>=a and b>=c:
    maior=b
if c>=a and c>=b:
    maior=c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

#Codigo que eu fiz para o disafio
'''v1=int(input('Digite um valor: '))
v2=int(input('Digite outro valor: '))
v3=int(input('Digite mais um valor: '))
if v1==v2==v3:
    print('Todos os números são iguais.')
if v1>v2 and v1>v3:
    print(f'O maior número é {v1}')
if v1<v2 and v1<v3:
    print(f'O menor número é {v1}')
if v2>v1 and v2>v3:
    print(f'O maior número é {v2}')
if v2<v1 and v2<v3:
    print(f'O menor número é {v2}')
if v3>v1 and v3>v2:
    print(f'O maior número é {v3}')
if v3<v1 and v3<v2:
    print(f'O menor número é {v3}')
if v1==v2 or v1==v3:
    if v1>v3 or v1>v2:
        print(f'O maior número é {v1}')
    if v1<v3 or v1<v2:
        print(f'O menor número é {v1}')
if v2==v3:
    if v3>v1:
        print(f'O maior número é {v3}')
    if v3<v1:
        print(f'O menor número é {v3}')'''