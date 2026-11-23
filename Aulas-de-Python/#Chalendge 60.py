n = int(input("\nEnter a number: "))
b = n
e = n
v = 0
#print("valor do e: ",e)
while n != 1:
    n -= 1
    #print("valor do novo n: ",n)
    #print()

    v = n
    #print("valor do v: ",v)
    #print()
    
    e = e * v
    #print("valor do novo e: ",e)
    #print()
    
print(f"{b}! is = {e}\n")
