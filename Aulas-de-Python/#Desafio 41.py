#Desafio 41
from datetime import date
yn = int(input('Type your birth year: '))
age = date.today().year - yn
if age <= 9:
    print(f'\nYou are {age} year old.\nYou are a Mirin swimmer!\n')
elif 9 < age <= 14:
    print(f"\nYou are {age} year old.\nYou are a Children swimmer!\n")
elif 14 < age <= 19:
    print(f"\nYou are {age} year old.\nYou are a Junior swimmer!\n")
elif age == 20:
    print(f"\nYou are {age} year old.\nYou are a Senior swimmer!\n")
elif age > 20:
    print(f"\nYou are {age} year old.\nYou are a Master swimmer!\n")