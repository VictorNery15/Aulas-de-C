#Desafio 36
cv = float(input('\nValuer of the house: $'))
sv = float(input('\nYour salary: $'))
at = int(input('\nFor how many years will you be paying: '))
mp = (cv / at)/12  
s30 = sv*(30/100)
if mp < s30:
    print('\n','='*80,f"\n 30% of a ${sv:.2f} salary is ${s30:.2f}\n \n You can buy a house of ${cv:.2f} for {at:.0f} years paying ${mp:.2f} for month.\n",'='*80,'\n')
else:
    print('='*80,f"\n 30% of a ${sv:.2f} salary is ${s30:.2f}\n \n So you can't buy a house of ${cv:.2f} for {at:.0f} years, cause is how much ${mp:.2f} for month and it's more that 30% of your salary.\n",'='*80,"\n")