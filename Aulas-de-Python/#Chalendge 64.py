n = 0
s = 0
c = 0
print()
while n != 999:
    c += 1
    if c > 1:
        n = int(input("Enter other number: "))
    else:
        n = int(input("Enter a number: "))
    s += n
    print("\n If you want stop type 999\n")
print(f"Plus of the {c-1} numbers that you enter is {s-999}\n")