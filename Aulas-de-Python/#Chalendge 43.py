#Chalendge 43
h = float(input("Enter your height (m): "))
w = float(input("Enter your weight (Kg): "))
imc = w / h**2
if imc < 18.5:
    print(f"\nYou need to gain weight!\nYour IMC is {imc:.1f}, that's very low!\n")
elif 18.5 <= imc < 25:
    print(f"\nYou are very good!\nYour IMC is {imc:.1f}, that's a good score!\n")
elif 25 <= imc < 30:
    print(f"\nYou are huge right!\nYour IMC is {imc:.1f}, be careful, it might be bad!\n")
elif 30 <= imc < 40:
    print(f"\nYou really need to lose weight!\nYour IMC is {imc:.1f}, that's a lot, it could be dangerous!\n")
else:
    print(f"\nYou need to lose weight right now!\nYour IMC is {imc:.1f}, that's very dangerous!\n")