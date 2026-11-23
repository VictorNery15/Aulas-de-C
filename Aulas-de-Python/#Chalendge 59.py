print('=-'*20)
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo Valor: "))

maior = n1 < n2
opcao = 0

while opcao != 5:
    print('=-'*20)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maoir
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
    opcao = int(input("Qual é sua opção: "))
    print('=-'*20)
    if opcao == 1:
            print(f'{n1} + {n2} = {n1+n1}.')
    elif opcao == 2:
            print(f'{n1} x {n2} = {n1*n2}.')
    elif opcao == 3:
            if maior is True:
                print(f"{n2} é maior que {n1}.")
            else:
                print(f"{n1} é maior que {n2}.")
    elif opcao == 4:
            print('Infome os novos números:')
            n1 = int(input('Primeiro valor:'))
            n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print("Encerrando o programa.")
    else:
        print('Error!!! Escolha apenas entre as opções disponiveis.')
    print()




'''
o = 0
while o != 5:
    print("=-"*15)
    o = int(input("Choose an operetion:\n[1] plus\n[2] multiplication\n[3] The biggest number\n[4] The smaller number\n[5] Shut out\nYou choose: "))
    
    if o > 5 or o < 1:
        print("=-"*15,'\n')
        print("\033[1;31m!\033[m"*40)
        print("Please choose only the options presented.")
        print("\033[1;31m!\033[m"*40,"\n")
    elif o != 5:
        n1 = float(input("\nEnter a number: "))
        n2 = float(input("Enter other number: "))
        v = n1 > n2
        if o == 1:
            print(f"\n\033[1;33m{n1} plus {n2} is {n1+n2:.2f}\033[m")
        elif o == 2:
            print(f"\n\033[1;33m{n1} multiplication for {n2} is {n1*n2:.2f}\033[m")
        elif o == 3:
            if v is True:
                print(f"\n\033[1;33mThe biggest number is {n1}\033[m")
            else:
                print(f"\n\033[1;33mThe biggest number is {n2}\033[m")
        else:
            if v is False:
                print(f"\n\033[1;33mThe smaller number is {n1}\033[m")
            else:
                print(f"\n\033[1;33mThe smaller number is {n2}\033[m")
'''