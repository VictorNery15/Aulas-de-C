#Desafio 40
n1 = float(input('Enter your score: '))
n2 = float(input('Enter your other score: '))
ave = (n1 + n2) / 2
if ave < 5:
    print(f'\nYou falied.\nYou need get a median of 5.0 points and your median is {ave:.1f}\n')
elif 5 <= ave < 7:
    print(f"\nYour median is {ave:.1f} points.\nIt's low, you will need to do remedial work\n")
elif 7 < ave <= 10:
    print(f"\nCongratulations!\nYour median is {ave:.1f} point.\nIt's really cool!\n")
elif ave > 10:
    print(f"\nHey dont lie!\nThe maximun score is 10 and did you say that you have {ave:.1f} point?\n")