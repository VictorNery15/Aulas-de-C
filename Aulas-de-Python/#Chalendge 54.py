#Chalendge 54
from datetime import date
a = 0 
b = 0
yn = date.today().year
print()
for q in range(1,8):
    y = int(input((f"Type the birth year of the {q}ª person: ")))
    ag = yn - y
    if ag < 20:
        a += 1
    else:
        b += 1
print(f"\n{b} are 20 years of age or older\n")
print(f"\n{a} are not 20 years of age or older\n")