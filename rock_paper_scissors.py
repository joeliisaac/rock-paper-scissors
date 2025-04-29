import random

#rules
# Rock(1) beats Scissors(3).
# Scissors(3) beat Paper(2).
# Paper(2) beats Rock(1).

#player can select 
# 1 for rock
# 2 for papers 
# 3 for scissors
print("====================\nROCK PAPER SCISSORS\n====================")

player = int(input("1 for rock\n2 for paper \n3 for scissors\nEnter a value: "))
computer = random.randint(1,3)

print(f'you choose: {player}')
print(f'CPU choose: {computer}')

if player > 3 :
    print("Invalid input!")
elif player == 1 and computer == 3:
    print("The player won!")
elif player == 3 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif player == computer and computer == player:
    print("DRAW!")
else:
    print("The CPU won!")




#rules
# Scissors(3) cut Paper(2).
# Paper(2) covers Rock(1).
# Rock(1) crushes Lizard(4).
# Lizard(4) poisons Spock(5).
# Spock(5) smashes Scissors(3).
# Scissors(3) beat Lizard(4).
# Lizard(4) eats Paper(2).
# Paper(2) disproves Spock(5).
# Spock(5) vaporizes Rock(1).
# Rock(1) breaks Scissors(3).

#player can select 
# 1 for rock
# 2 for papers 
# 3 for scissors
# 4 for lizard
# 5 for spock

print("====================\nROCK PAPER SCISSORS LIZARD SPOCK\n====================")

player = int(input("1 for rock\n2 for paper \n3 for scissors\n4 for lizard\n5 for spock\nEnter a value: "))
computer = random.randint(1,5)

print(f'you choose: {player}')
print(f'CPU choose: {computer}')


if player > 5 :
    print("Invalid input!")
elif player == 3 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif player == 1 and computer == 4:
    print("The player won!")
elif player == 4 and computer == 5:
    print("The player won!")
elif player == 5 and computer == 3:
    print("The player won!")
elif player == 3 and computer == 4:
    print("The player won!")
elif player == 4 and computer == 2:
    print("The player won!")
elif player == 2 and computer == 5:
    print("The player won!")
elif player == 5 and computer == 1:
    print("The player won!")
elif player == 1 and computer == 3:
    print("The player won!")
elif player == computer and computer == player:
    print("DRAW!")
else:
    print("The CPU won!")

