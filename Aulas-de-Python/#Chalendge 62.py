print("Creater of arithmetic progression\n")
i = int(input("Enter the Intial Term: "))
d = int(input("Enter the Common Diference: "))
print()
ch = 10
c = 0

while ch != 0:
    while c != ch:
        print("=- ",i," -=",end='')
        c += 1
        i += d
    ch = 1
    if ch == 1:
        ch = int(input("\n\nIf you want to see more terms, type how many, if not type 0.\nENTER HERE -->: "))
        print()
        c = 0

    if ch <= -1 :
        print("\033[1;31m!!!!Err!!!!\033[m\n")
        while not ch > -1:
            ch = int(input("Please type 0 or positive number: "))
            print()
