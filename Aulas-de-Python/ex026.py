f=str(input('Digite uma frase: ')).strip().lower()
print(f'A letra "A" aparece {f.count('a')} vezes na frase')
print(f'A primera aparição dessa letra foi na posição {f.find('a')+1}')
print(f'E a ultima foi na posição {f.rfind('a')+1}')