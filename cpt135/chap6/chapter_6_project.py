#Braden Evans
import math

def input_choice(prompt, options):
    opts = [o.lower() for o in options]
    while True:
        c = input(prompt).strip().lower()
        if c in opts:
            return c
        print(f"Please enter one of: {', '.join(options)}")
