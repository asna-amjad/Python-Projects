## Project 4 - Rock Paper Scissors

import random

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
'''
paper = '''
         ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'      
'''
scissor = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
game_images = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for scissor.\n"))
# 0, 1, 2
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"computer choice: ")
print(game_images[computer_choice])

if user_choice >=3 and user_choice < 0:
    print("you mentioned an invalid choice. You lose!")
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a tie!")
