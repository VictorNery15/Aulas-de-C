from random import randint
cn = randint(0,10)
jn = cn+1
t = 0
print("\nVamos jogar um jogo!!\n\nO computador pensou em um numero de 0 a 10! Tente adivinhalo.")
while jn != cn:
    jn = int(input('--> '))
    t += 1
    if jn < cn:
        print("\nResposta errada! Talvez um numero maior ...\nTente novamente!")
    elif jn > cn:
        print("\nRespsta errada! Talvez um numero menor ...\nTente novamente!")
print(f"\nParabens voce ganhou depois de {t} tentativas")

if t <= 3:
    print("Voce é bom.  =O\n")
elif 3 < t <= 6:
    print("Eh da pra melhorar.  =P\n")
elif t > 6:
    print("voce e muito ruin kk.  XP\n") 