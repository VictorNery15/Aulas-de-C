#Chalendge 51
print("\nCreater of arithmetic progression.")
f = int(input("\nType the Initial term of A.P: "))
d = int(input("\nType the Common diference: "))
print(f"\nThese are the 10 fisrt term:\n{f}")
for ap in range(1,10):
    f += d
    print(f)