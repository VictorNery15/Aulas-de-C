#Chalendge 37
n0 = int(input('\nType in a number: '))
print("\nChoose one to convert:")
print("| 1 | convert to Binary\n| 2 | convert to Octal\n| 3 | convert to hexadecimal\n")
ch = int(input("Your Choose: "))
if ch == 1:
    print(f'The number "{n0}" convert to "{n0:b}" in Binary.')
    #print(bin(n0)[2:]) work too
elif ch == 2:
    print(f'The number "{n0}" convert to "{n0:o}" in Octal.')
    #print(oct(n0)[2:]) work too
elif ch == 3:
    print(f'The number "{n0}" convert to "{hex(n0)[2:]}" in Hexadecimal.')
else:
    print("\n!!!Please, Choose only one of the 3 option!!!\n")