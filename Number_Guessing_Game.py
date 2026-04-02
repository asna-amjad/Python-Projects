import random
from art import logo

### The Number Guessing Game
def guess_number():
    global your_guess

    print(f"Welcome to the Number Guessing Game!")
    print(logo)
    result = random.randint(1, 100)       # Choose a random number between 1 and 100
    print(f"I am thinking of a number between 1 and 100.")

    # Difficulty Level Selection
    user_choice  = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if user_choice == 'easy':
        your_guess = 10
    elif user_choice == 'hard':
        your_guess = 5
    else:
        print("Invalid choice.")
        your_guess = 10

    # While Loop to play the Game
    while your_guess > 0:
            print(f"You have {your_guess} attempts left to guess the number.")
            attempt = int(input("Enter your Guess: "))

            if attempt > result:
                print(f"Too high!")
                print(f"Guess again.")
                #print(f"You have {attempt - 1} attempts remaining.")
            elif attempt < result:
                print(f"Too low!")
                print(f"Guess again.")
                #print(f"You have {attempt - 1} attempts remaining.")
            else:
                print(f"Correct! You guessed the number {result}.")
            if your_guess == 0:
                print(f"Game Over! The number was {result}.")
                break
                
            your_guess -= 1

    # Play Gamer again
    play_again = input("Would you like to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        print("\n" * 100)
        guess_number()
    else:
        print(f"Thank you for playing!")

guess_number()
