#Desafio 39
from datetime import date
year = int(input('Enter the year you were born: '))
age = date.today().year - year
yn = date.today().year
if age < 18:
    print(f"\nYou not being ready, yet\nLeft {18-age} years\nWill happen in {yn+(18-age)}")
elif age == 18:
    print(f'\nCongratulations!\nYou are an adult now and you need to go register for military services now\n')
elif age > 18:
    print(f'\nYou are later!\nHave you forgetten your resposability?\nWe have been waiting for {age-18} years\nIt should have been in {yn-(age-18)}')