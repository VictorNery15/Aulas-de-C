from random import shuffle
a1=input('Primeiro aluno:')
a2=input('Segundo aluno:')
a3=input('Terceiro aluno:')
a4=input('Quarto aluno:')
l=[a3,a2,a1,a4]
shuffle(l)
print(f'A ordem é:\n{l}')