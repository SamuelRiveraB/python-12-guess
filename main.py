import random

NUM = random.randint(0,100)

def guessing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == "easy":
        count = 10
    else:
        count = 5
    while count > 0:
        guess = int(input("Make a guess: "))
        if(guess > NUM):
            print("Too high.")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number")
        elif(guess < NUM):
            print("Too low.")
            count -= 1
            print(f"You have {count} attempts remaining to guess the number")
        elif(guess == NUM):
            print(f"You got it, the answer was {NUM}")
            return
    print(f"You lost. The answer was {NUM}")

guessing()