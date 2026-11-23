#Chalendge 53
p = str(input("\nType a phrase: ")).strip().upper()
s = p.split()
j = ''.join(s)
i = ""

for l in range(len(j)-1,-1,-1):
    i += j[l]
print(f"\nThe reverse of \033[1;31m{j}\033[m is \033[1;33m{i}\033[m")
if j == i:
    print("This sentence is a polindrome.\n")
else:
    print("This sentence is not a polindrome.\n")
