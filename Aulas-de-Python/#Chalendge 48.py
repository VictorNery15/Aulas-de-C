#Chalendge 48
print("\nThat is the sum of all odd numbers mutiplying for 3 from 1 to 500.\n")
n = 0
for s in range(1,501,2):
    if s % 3 == 0:
        n += s 
print(n)
print()