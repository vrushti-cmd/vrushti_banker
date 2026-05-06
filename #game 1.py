#game 1
import random

secret_number = random.randint(1, 50)
attempts = 10
count = 0

print("Number Guessing Game.\n Guess a number between 1 and 50")
print("You have 10 attempts")

while count < attempts:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess == secret_number:
        print(f" Correct! You guessed it in {count} attempts")
        break
    elif guess < secret_number:
        print(" Too low!")
    else:
        print(" Too high!")

    print(f"Attempts left: {attempts - count}\n")

if count == attempts and guess != secret_number:
    print(f" Game Over! The number was {secret_number}")