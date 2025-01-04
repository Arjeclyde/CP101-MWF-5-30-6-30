import random

def guess_the_number():
    target_number = random.randint(1, 20)
    incorrect_number = target_number + 1  

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 20, but you will never guess it correctly. Try anyway!")

    for attempt in range(3):
        guess = int(input(f"Attempt {attempt + 1}: Your guess: "))
        
        if guess < target_number:
            print("Too low! Guess again.")
        elif guess > target_number:
            print("Too high! Guess again.")
        else:
            print(f"Whoops, you're not supposed to guess it correctly! Try again.")
            return

    print(f"Out of attempts! The number was {target_number}. Better luck next time.")

guess_the_number()
