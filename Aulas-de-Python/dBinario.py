#
bn = int(input("\nDigite um numero em binario de 8 digitos: "))
q = 0
v = 0

while v != 1:
    q = int(input('\nSe esse numero tiver complemento de 2 digite [1] se não digite [2]: '))
    if q == 1:
        v = 1
    elif q == 2:
        v = 1
    else:
        print("\nEscolha uma alternativa valida.")


un1 = bn // 1 % 10
un2 = bn // 10 % 10
un3 = bn // 100 % 10
un4 = bn // 1000 % 10
un5 = bn // 10000 % 10
un6 = bn // 100000 % 10
un7 = bn // 1000000 % 10
un8 = bn // 10000000 % 10
sm = 0
dec = '0'
b = '1'

if un7 == 1:
    sm += 64
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un6 == 1:
    sm += 32
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un5 == 1:
    sm += 16
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un4 == 1:
    sm += 8
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un3 == 1:
    sm += 4
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un2 == 1:
    sm += 2
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un1 == 1:
    sm += 1
    dec += ' 0'
    b += ' 1'
else:
    dec += ' 1'
    b += ' 0'

if un8 == 1:
    sm *= (-1)

dec = dec.split()
b = b.split()
b = ' | '.join(b)


if dec[7] == '0':
    dec[7] = dec[7].replace('0','1')
else:
    dec[7] = dec[7].replace('1','0')
    if dec[6] == '0':
        dec[6] = dec[6].replace('0','1')
    else:
        dec[6] = dec[6].replace('1','0')
        if dec[5] == '0':
            dec[5] = dec[5].replace('0', '1')
        else: 
            dec[5] = dec[5].replace('1','0')
            if dec[4] == '0':
                dec[4] = dec[4].replace('0', 1)
            else:
                dec[4] = dec[4].replace('1','0') 
                if dec[3] == '0':
                    dec[3] = dec[3].replace('0', 1)
                else:
                    dec[3] = dec[3].replace('1','0') 
                    if dec[2] == '0':
                        dec[2] = dec[2].replace('0', 1)
                    else:
                        dec[2] = dec[2].replace('1','0') 
                        if dec[1] == '0':
                            dec[1] = dec[1].replace('0', '1')#'''

if q == 1:
    sm = 0

    if dec[1] == '1':
        sm += 64
    if dec[2] == '1':
        sm += 32
    if dec[3] == '1':
        sm += 16
    if dec[4] == '1':
        sm += 8
    if dec[5] == '1':
        sm += 4
    if dec[6] == '1':
        sm += 2
    if dec[7] == '1':
        sm += 1

    

if q == 2:
    print('\nO numero binario:')
    print(f'\n{un8} | {un7} | {un6} | {un5} | {un4} | {un3} | {un2} | {un1}\n')
    print(f'Equivale a {sm} em decimal.\n')

else:
    print('\nO numero binario:')
    print(f'\n{b}\n')
    print(f'Equivale a -{sm} ou {sm} em decimal.\n')