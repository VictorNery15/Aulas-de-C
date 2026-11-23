n = 0
m = 0
ma = 0
me = 0
s = ''
c = 0

while s != '1':
    n = int(input("\nEnter a number: "))
    if s == '1':
        ma = n
        me = n
    else:
        if ma > n:
            ma = n
        if me < n:
            me = n
    m += n
    c += 1
    s = input("\nIf you want to stop type 1, if you want to keep type anything: ")
print(f"\nThe mediam is {m/c:.2f}")
print(f"The bigger number is {ma}\nThe lower number is {me}")