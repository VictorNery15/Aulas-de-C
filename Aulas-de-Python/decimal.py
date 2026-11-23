#decimal para binario
import os
dc = 0
while(dc <= 0):
    dc = int(input("\nDigite um numero em decimal: "))
    if dc <= 0:
        print("!!Erro!!\nApenas numeros positivos. Tente novamente.")
ct = 0
ts = 0
tts = dc

print()
while(ct != 8):

    ct += 1 

    if ct == 1:
        if tts < 128:
            print("0", end='')
        else:
            ts = tts - 128
            print("1", end='')
            tts = ts
        
    elif ct == 2:
        if tts < 64:
            print("0", end='')
        else:
            ts = tts - 64
            print("1", end='')
            tts = ts
                
    elif ct == 3:
        if tts < 32:
            print("0", end='')
        else:
            ts = tts - 32
            print("1", end='')
            tts = ts
                
    elif ct == 4:
        if tts < 16:
            print("0", end='')
        else:
            ts = tts - 16
            print("1", end='')
            tts = ts

    elif ct == 5:
        if tts < 8:
            print("0", end='')
        else:
            ts = tts - 8
            print("1", end='')
            tts = ts

    elif ct == 6:
        if tts < 4:
            print("0", end='')
        else:
            ts = tts - 4
            print("1", end='')
            tts = ts

    elif ct == 7:
        if tts < 2:
            print("0", end='')
        else:
            ts = tts - 2
            print("1", end='')
            tts = ts

    elif ct == 8:
        if tts < 1:
             print("0", end='')
        else:
            print("1", end='')
print("\n")
