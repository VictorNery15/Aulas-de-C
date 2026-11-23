v=input('Digite algo:')
print('O tipo primitivo desse valor é',type(v))
a1=v.isspace()

a3=v.isalpha()

a5=v.isupper()

a7=v.istitle()
print('Só tem espaço? {}'.format(a1))
print('Só tem numeros?',v.isnumeric())
print('Só tem letras? {}'.format(a3))
print('É alfanumérico?',v.isalnum())
print('Estár em maiúsculo? {}'.format(a5))
print('Estár em minúsculo?',v.islower())
print('Estár capitalizada {}'.format(a7))

