## Project 3 - Treasure Island
## Based on Treasure Island Flowchart

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where would you like to go? '
                'Type "left" or "right".\n').lower()

if choice1 == 'left':
    choice2 = input('You\'ve come in the middle of the lake. '
          'Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        choice3 = input("You need to select a door before moving forward. "
                        "There is a house with 3 doors. Red, yellow and blue. "
                        "Which door would you like to go?\n").lower()
        if choice3 == 'red':
            print("Room not available. Game Over!")
        elif choice3 == 'yellow':
            print("You found the treasure. You Win!")
        elif choice3 == 'blue':
            print("You entered the wrong room. Game Over!")
        else:
            print("You chose an invalid choice.")
    else:
        print("You encountered a trout. Game Over!.")
else:
    print("Game over!")
