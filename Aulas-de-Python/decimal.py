#decimal para binario
import os
dc = -128
q = 1
v = 0

while(dc < -127 or dc > 127):
    dc = int(input("\nDigite um numero em decimal entre -127 e 127: "))
    if (dc < -127 or dc > 127):
        print("\nEscolha um numero valido.")

if dc == 0:
    while(v != 1):
        q = int(input("\nEscolha (1) para [-0] ou (2) para [+0]: "))
        if q == 1:
            v = 1
        elif q == 2:
            v = 1
        else:
            print("\nEscolha uma alternativa valida.")


ct = 0
ts = 0
tts = dc
bc = ''


print("\nNumero binario:")
while(ct != 8):

    ct += 1 

    if dc == 0 and q == 1:
        print('1`00000000', end='')
        bc = ' 0 0 0 0 0 0 0'
        ct += 7

    if dc == 0 and q == 2:
        print('0`00000000', end='')
        ct += 7

    if ct == 1:
        if tts > 0:
            print("0`", end='')
            bc +=' 1`'
            
        else: 
            print("1`", end='')
            bc += ' 1`'
            tts = tts * -1

    elif ct == 2:
        if tts < 64:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 64
            print("1", end='')
            bc += ' 0'
            tts = ts
                
    elif ct == 3:
        if tts < 32:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 32
            print("1", end='')
            bc += ' 0'
            tts = ts
                
    elif ct == 4:
        if tts < 16:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 16
            print("1", end='')
            bc += ' 0'
            tts = ts

    elif ct == 5:
        if tts < 8:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 8
            print("1", end='')
            bc += ' 0'
            tts = ts

    elif ct == 6:
        if tts < 4:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 4
            print("1", end='')
            bc += ' 0'
            tts = ts

    elif ct == 7:
        if tts < 2:
            print("0", end='')
            bc += ' 1'
        else:
            ts = tts - 2
            print("1", end='')
            bc += ' 0'
            tts = ts

    elif ct == 8:
        if tts < 1:
            if dc == 0:
                bc += ' 0'
            else:   
                print("0", end='')
                bc += ' 1'
             
        else:
            print("1", end='')
            bc += ' 0'

print("\n\nComplemento de 2:")

bc = bc.split()


if dc <= 0 and q == 1:

    if bc[7] == '0':
        bc[7] = bc[7].replace('0','1')
    else:
        bc[7] = bc[7].replace('1','0')
        if bc[6] == '0':
            bc[6] = bc[6].replace('0','1')
        else:
            bc[6] = bc[6].replace('1','0')
            if bc[5] == '0':
                bc[5] = bc[5].replace('0', '1')
            else: 
                bc[5] = bc[5].replace('1','0')
                if bc[4] == '0':
                    bc[4] = bc[4].replace('0', 1)
                else:
                    bc[4] = bc[4].replace('1','0') 
                    if bc[3] == '0':
                        bc[3] = bc[3].replace('0', 1)
                    else:
                        bc[3] = bc[3].replace('1','0') 
                        if bc[2] == '0':
                            bc[2] = bc[2].replace('0', 1)
                        else:
                            bc[2] = bc[2].replace('1','0') 
                            if bc[1] == '0':
                                bc[1] = bc[1].replace('0', '1')
                            #'''

    bc = ''.join(bc)
    if dc == 0:
        bc = '00000000'
    
    print(bc)
    print()

else:
    print("Sem complemento de 2. Pois o numero e positivo.\n")
