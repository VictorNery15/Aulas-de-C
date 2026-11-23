#Chalendge 52
n = int(input("\nType a integer number: "))
if n <= 1:
    print("\nThis is not a prime number.\n")
elif n == 2 or n == 3:
    print("\nThis is a prime number.\n")
elif n % 2 == 1:
    if n % 3 >= 1:
        print("\nThis is a prime number.\n")
    else:
        print("\nThis is not a prime number.\n")
else:
    print("\nThis is not a prime number.\n")