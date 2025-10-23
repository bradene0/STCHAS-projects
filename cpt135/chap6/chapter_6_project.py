#Braden Evans
import math

def input_choice(prompt, options):
    opts = [o.lower() for o in options]
    while True:
        c = input(prompt).strip().lower()
        if c in opts:
            return c
        print(f"Please enter one of: {', '.join(options)}")
def input_positive_number(prompt):
    while True:
        try:
            v = float(input(prompt).strip())
            if v > 0:
                return v
            print("Value must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_area_of_square(length):
    return length * length

def calculate_area_of_rectangle(length, width):
    return length * width

def calculate_area_of_circle_by_radius(radius):
    return math.pi * radius * radius

def calculate_volume(area, thickness):
    return area * thickness

def circle_area_prompt(unit):
    mode = input_choice("Will you enter 'radius' or 'diameter'?: ", ["radius", "diameter"])
    val = input_positive_number(f"Enter {mode} ({unit}): ")
    r = val if mode == "radius" else val / 2.0
    return calculate_area_of_circle_by_radius(r)

def main():
    shape = input_choice("Choose a cookie shape (circle, square, rectangle): ", ["circle", "square", "rectangle"])
    measure = input_choice("Do you want 'area' or 'volume'?: ", ["area", "volume"])
    unit = input_choice("Units (mm, cm, inches): ", ["mm", "cm", "inches"])

    area = {
        "circle": lambda: circle_area_prompt(unit),
        "square": lambda: calculate_area_of_square(input_positive_number(f"Enter side length ({unit}): ")),
        "rectangle": lambda: calculate_area_of_rectangle(
            input_positive_number(f"Enter length ({unit}): "),
            input_positive_number(f"Enter width ({unit}): ")
        )
    }[shape]()

    value = area if measure == "area" else calculate_volume(area, input_positive_number(f"Enter thickness ({unit}): "))
    units_power = {"area": "^2", "volume": "^3"}[measure]
    print(f"{measure.capitalize()}: {round(value, 1)} {unit}{units_power}")

if __name__ == "__main__":
    main()        
