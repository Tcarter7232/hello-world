import math

def get_bounds():
    """Get the lower and upper bounds from the user."""
    while True:
        try:
            lower_bound = int(input("Enter the lower bound: "))
            upper_bound = int(input("Enter the upper bound: "))
            if lower_bound < upper_bound:
                return lower_bound, upper_bound
            else:
                print("Invalid bounds. Please ensure the lower bound is less than the upper bound.")
        except ValueError:
            print("Invalid input. Please enter integers for the bounds.")

def get_hint(guess, lower_bound, upper_bound):
    """Get a hint from the user about the guess."""
    while True:
        hint = input(f"Is your number {guess}? (h)igher, (l)ower, or (c)orrect: ")
        if hint.lower() == 'h':
            return 'higher'
        elif hint.lower() == 'l':
            return 'lower'
        elif hint.lower() == 'c':
            return 'correct'
        else:
            print("Invalid hint. Please enter 'h' for higher, 'l' for lower, or 'c' for correct.")

def guess_number(lower_bound, upper_bound):
    """Guess the number thought of by the user."""
    min_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"Minimum number of guesses needed: {min_guesses}")
    
    for _ in range(min_guesses):
        guess = (lower_bound + upper_bound) // 2
        hint = get_hint(guess, lower_bound, upper_bound)
        if hint == 'higher':
            lower_bound = guess + 1
        elif hint == 'lower':
            upper_bound = guess - 1
        elif hint == 'correct':
            print(f"Yay! I guessed the number in {_ + 1} attempts.")
            return

    print("I couldn't guess the number. You might have entered misleading hints.")

def main():
    lower_bound, upper_bound = get_bounds()
    guess_number(lower_bound, upper_bound)

if __name__ == "__main__":
    main()
