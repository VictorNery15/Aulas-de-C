#Chalendge 55
b = 0
l = 11000
for q in range(1,6):
    w = int(input("Type your weight (Kg): "))
    if w > b:
        b = w
    if w < l:
        l = w
print(f"the bigger weight is {b}")
print(f"The lower weight is {l}")