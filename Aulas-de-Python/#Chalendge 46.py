#Chalendge 46
from time import sleep
q = input("YOU'RE READY TO THE FIREWORKS?!? YES/NOT?: ").strip()
v = q.isalpha
if v() == True:
    q = q.lower()
if q == 'yes':
    print("\nHELL YEAH MAN!! ")
    sleep(1)
    print("SO LET'S GO!!\n")
    sleep(1)
elif q == 'not':
    print("\nREALLY?? ")
    sleep(1)
    print("But anyway. ")
    sleep(1)
    print("WE GONNA DO!! ")
    sleep(1)
    print("LET'S GOOO!!\n")
    sleep(1)
else:
    print("\nWHAT?!? ")
    sleep(1)
    print("Whatever! ")
    sleep(1)
    print("LET'S GOOO!!\n")
    sleep(1)
for C in range(10,0,-1):
    print(C)
    sleep(1)
print("\nFIREWORKS!!!\n")