import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    
    # Get the range from the user
    while True:
        try:
            lb = int(input("Enter the lower bound of the range: "))
            ub = int(input("Enter the upper bound of the range: "))
            
            if lb >= ub:
                print("The lower bound should be less than the upper bound. Please try again.")
            else:
                break
        except ValueError:
            print("Please enter valid numbers for the range.")
    
    # Generate a random number within the specified range
    number_to_guess = random.randint(lb, ub)
    guess = None

    print(f"I'm thinking of a number between {lb} and {ub}. Can you guess it?")
    
    # Main game loop
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the correct number.")
        except ValueError:
            print("Please enter a valid number.")
    
guess_the_number()
