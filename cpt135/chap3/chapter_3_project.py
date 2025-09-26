# Braden Evans
import math 

COVERAGE_PER_GALLON = 350

paint_price = {
    "blue": 50,
    "orange": 25,
    "purple": 30,
    "gray": 12.99,
    "tan": 20,
    "white": 25
}


wall_length = float(input("Please enter the wall length in feet"))
ceiling_height = float(input("Please enter the ceiling height in feet"))
color_choice  =  input("Please enter the color you wish to use, (blue, orange, purple, gray, tan, white")
wall_area = ceiling_height * wall_length
wall_area =round(wall_area)

paint_needed = wall_area / COVERAGE_PER_GALLON
paint_needed = round(paint_needed, 2)
cans_needed = math.ceil(paint_needed)

if color_choice in paint_price:
    total_cost = paint_price[color_choice] * cans_needed
    print(f"Using {color_choice} paint will cost: ${round(total_cost)}")
else:
    print("Please enter a color from the list provided")



