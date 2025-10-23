#Braden Evans
import random

def get_valid_guess():
    while True:
        s = input("Enter a number 1-100: ").strip()
        try:
            g = int(s)
            if 1 <= g <= 100:
                return g
            else:
                print("Invalid: enter an integer between 1 and 100.")
        except ValueError:
            print("Invalid: enter an integer between 1 and 100.")

def play_round():
    target = random.randint(1, 100)
    for attempt in range(1, 21):
        guess = get_valid_guess()
        remaining = 20 - attempt
        if guess == target:
            print(f"Correct! You got it in {attempt} guess{'es' if attempt != 1 else ''}.")
            return attempt
        elif guess < target:
            print(f"You are too low. Guesses left: {remaining}")
        else:
            print(f"Too high. Guesses left: {remaining}")
    print(f"No more guesses! The number was {target}.")
    return None

def main():
    high_score = None
    while True:
        ans = input("Play? (y/n): ").strip().lower()
        if ans != "y":
            break
        result = play_round()
        if result is not None:
            if high_score is None or result < high_score:
                high_score = result
                print(f"New high score: {high_score} guesses!")
            else:
                print(f"High score remains: {high_score} guesses.")
    print("Goodbye!")

if __name__ == "__main__":
    main()

