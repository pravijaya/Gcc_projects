import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set the range of the numbers and the number of attempts
    min_number = 1
    max_number = 100
    max_attempts = 10
    
    # Generate the random number to guess
    secret_number = random.randint(min_number, max_number)
    
    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1}/{max_attempts}")
        
        # Get the player's guess
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if min_number <= guess <= max_number:
                    break
                else:
                    print(f"Please enter a number between {min_number} and {max_number}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Try again. The secret number is higher.")
        else:
            print("Try again. The secret number is lower.")
    else:
        print(f"\nSorry, you ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
