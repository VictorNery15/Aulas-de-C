print("\nLet's see a Fibonacci Sequence!!\n")
n = int(input("Enter a number: "))
q = int(input("Enter how many elements it will appear: "))
print()
c = 0
m = n
b = n
o = n
c2 = 0
while c != q:
    c += 1
    if c > 2:
        if c > 3:
            m = o
            o = o + b
            b = m
        else:
            o = n + n
    print('-=',o,'=-',end='')
print("\n")
