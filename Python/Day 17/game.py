import random

# Generate a random 3-digit number with no repeating digits.
digits = list(range(10))
random.shuffle(digits)
secret_number = ''.join(map(str, digits[:3]))

print("Welcome to the Number Guessing Game!")
print("I've generated a 3-digit number with no repeating digits.")
print("Try to guess it!")

while True:
    # Get the user's guess.
    guess = input("Enter your 3-digit guess: ")

    if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
        print("Invalid input. Please enter a valid 3-digit number with no repeating digits.")
        continue

    # Check the guess and give clues.
    clues = []
    for i in range(3):
        if guess[i] == secret_number[i]:
            clues.append("Match")
        elif guess[i] in secret_number:
            clues.append("Close")
        else:
            clues.append("Nope")

    # Print the clues.
    for clue in clues:
        print(clue)

    # If the guess is correct, break out of the loop.
    if guess == secret_number:
        print("CODE CRACKED!")
        break
