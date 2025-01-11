import random

# Function to set difficulty and number range
def set_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return 50
            elif choice == 2:
                return 100
            elif choice == 3:
                return 200
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

# Function to provide hints after a certain number of wrong attempts
def provide_hint(secret_number, guess):
    if guess < secret_number:
        print("Hint: Try a higher number!")
    elif guess > secret_number:
        print("Hint: Try a lower number!")

# Main game function
def guess_the_number():
    print("Welcome to the extended 'Guess the Number' game!")
    
    # Set difficulty and the upper range based on difficulty
    upper_bound = set_difficulty()
    lower_bound = 1
    secret_number = random.randint(lower_bound, upper_bound)
    
    print(f"Guess the number between {lower_bound} and {upper_bound}.")
    
    attempts = 0
    max_attempts = 10  # Limit the number of attempts for the game
    previous_guesses = []  # To track previous guesses
    
    while attempts < max_attempts:
        try:
            # Ask for the player's guess
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
            if guess < lower_bound or guess > upper_bound:
                print(f"Your guess is out of range. Please choose a number between {lower_bound} and {upper_bound}.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        # Increment attempts and track the guess
        attempts += 1
        previous_guesses.append(guess)
        
        # Check if the guess is correct
        if guess < secret_number:
            print("Too low!")
            provide_hint(secret_number, guess)
        elif guess > secret_number:
            print("Too high!")
            provide_hint(secret_number, guess)
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break
        
        # Display previous guesses
        print(f"Your previous guesses: {', '.join(map(str, previous_guesses))}")
    
    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {secret_number}.")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
guess_the_number()
