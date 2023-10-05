#easy mode = 10 lives, hard mode = 5 lives
import random
from replit import clear
from artNumberGuessing import logo

number = random.randint(1, 100)
lives = 0
guess = False

clear()
print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")
print(f"The correct answer is {number} btw")

difficulty = input("Chopse a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    lives = 10
    print(f"You have {lives} attempts remaining to guess the number.")
elif difficulty == "hard":
    lives = 5
    print(f"You have {lives} attempts remaining to guess the number.")


while not guess:
    if lives > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Too high.")
            if lives > 0:
                print("Guess again.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number")
        elif user_guess < number:
            print("Too low.")
            lives -= 1
            if lives > 0:
                print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number")

        elif user_guess == number:
            print(f"You got it! The answer was {number}.")
            guess = True
    else:
        print("You've run out of guesses, you lose.")
        guess = True
        break