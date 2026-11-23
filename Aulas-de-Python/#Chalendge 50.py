#Chalendge 50
l = 0
print()
for c in range(1,7):
    n = int(input("Type a number: "))
    if n % 2 == 1:
        l += n
print(f"The sum of all odd numbers is {l}\n")