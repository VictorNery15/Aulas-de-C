n=str(input('Digite seu nome: '))
print(f'Seu nome tem Silva? {'silva' in n.lower()}')
'''''
n=str(input('Digite seu nome: ')).strip()
n=n.lower()
b=n.find('silva')
print(f'Seu nome tem Silva? {b>-1}')'''