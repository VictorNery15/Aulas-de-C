#Chalendge 45
import random
ch = int(input('''LETS PLAY A GAME!!
[1]ROCK
[2]PAPER
[3]SCISSORS
CHOISE ONE!!: '''))
pch = random.choice([1,2,3])
def tch():
    if ch == 1:
        return 'ROCK'
    if ch == 2:
        return 'PAPER'
    if ch == 3:
        return 'SCISSORS'
def tpc():
    if pch == 1:
        return 'ROCK'
    if pch == 2:
        return 'PAPER'
    if pch == 3:
        return 'SCISSORS'
if ch == 1 and pch == 3 or ch == 2 and pch == 1 or ch == 3 and pch == 2:
    print(f"\nYou win!\n\nYou: {tch()}\n\n    VS\n\nPC: {tpc()}\n")
elif pch == 1 and ch == 3 or pch == 2 and ch == 1 or pch == 3 and ch == 2:
    print(f"\nYou lose!\n\nYou: {tch()}\n\n    VS\n\nPC: {tpc()}\n" )
elif 1 == ch and pch or 2 == ch and pch or 3 == ch and pch:
    print(f"\nIt was a draw!\n\nYou: {tch()}\n\n    VS\n\nPC: {tpc()}\n")
else:
    print("\nYou problably spelled it wrong. Try again.\n")

''''ch = str(input(''LETS PLAY A GAME!!
[Rock]
[Paper]
[Scissors]
Choise one!!: '')).strip()
ch = ch.lower()
pch = random.choice(["rock","paper","scissors"])
if ch == "rock" and pch == "scissors" or ch == "paper" and pch == "rock" or ch == "scissors" and pch == "paper":
    print(f"\nYou win!\n\nYou: {ch}\n\n    VS\n\nPC: {pch}\n")
elif pch == "rock" and ch == "scissors" or pch == "paper" and ch == "rock" or pch == "scissors" and ch == "paper":
    print(f"\nYou lose!\n\nYou: {ch}\n\n    VS\n\nPC: {pch}\n" )
elif "rock" == ch and pch or "paper" == ch and pch or ch and pch == "scissors":
    print(f"\nIt was a draw!\n\nYou: {ch}\n\n    VS\n\nPC: {pch}\n")
else:
    print("\nYou problably spelled it wrong. Try again.\n")'''