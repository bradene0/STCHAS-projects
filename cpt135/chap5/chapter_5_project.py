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
