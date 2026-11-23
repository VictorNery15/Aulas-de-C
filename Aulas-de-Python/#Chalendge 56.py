#Chalendge 56
from datetime import date
yn = date.today().year
me = 0
ol = 0
oln = 0
wc = 0

for l in range(1,5):
    print("=-"*20,"\nTYPE YOUR DATA!!\n")
    na = str(input("Type your name: ")).strip()
    ag = int(input("Type your age: "))
    sex = int(input("Type 1 if you are man and 2 if you are wommen: ")) 
    print("=-"*20,"\n")
    me += ag
    if ag > ol:
        ol = ag
        oln = na
    if sex == 2:
        if ag < 20:
            wc += 1

oln = oln.capitalize()
print(F'\n{" SEARCH RESULT ":=^40}\n')
print(f"{oln} is the oldest!!")    
print(f"The averege age of the group is {me/4:.0f}!!")
print(f"There are {wc} wommen under the age of 20!!!\n")
