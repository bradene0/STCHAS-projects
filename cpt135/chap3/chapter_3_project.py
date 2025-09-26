# Braden Evans
import math 

COVERAGE_PER_GALLON = 350

paint_price = {
    "blue" = 50,
    "orange" = 30,
    "purple" = 5.99,
    "gray" = 12.99,
    "tan" = 20,
    "white" = 25,
}

wall_length = float(input("Please enter the wall length in feet"))
ceiling_height = float(input("Please enter the ceiling height in feet"))
wall_area = ceiling_height * wall_length
wall_area =roung(wall_area)
