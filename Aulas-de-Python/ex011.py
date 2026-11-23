n1=float(input('Descubra quantos litros de tinta você vai utilizar para pinta sua parede!\nDigite a altura da parede em metros: m='))
n2=float(input('Agora a largura: m='))
t=float(input('Um litro da sua tinta pinta quantos m²? m²='))
v1=n1*n2
l=v1/t
print(f'A dimensão da sua parede é de {n1:.2f}m X {n2:.2f}m\nSua área é de {v1:.2f}m².\nPara pinta essa parede, com essa tinta, você vai gastar {l:.2f}L de tinta.')
