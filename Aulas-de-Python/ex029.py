print('Você estar em um carro indo ao cinema.')
print('Porém falta pouco tempo para começar.')
v=float(input('Em quantos KM/H você vai? '))
if v <= 70:
    print('Você fez uma viagem segura, mas infelismente você não chegou a tempo. =(')
if 70<v<=80:
    print('Você dirigiu rapidamente mas com segurança, conseguindo chegar no seu destino a tempo. =D')
if v > 80:
    m=(v-80)*7
    print('Você pisou no acelerador sem se conter, porém, diante de tal ação inresponsável, os policias\ninterviram e você levou uma multa de 7 R$ para cada quilometro acima dos 80. >=C')