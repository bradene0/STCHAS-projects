#hotdog program Braden Evans
food1 = str(input("Please enter the first food item: "))
food1_price = float(input("Please enter the price for the first item: "))
food1_quantity = int(input("Please enter the number of first food you have: "))

food1_total = food1_price * food1_quantity

food2 = str(input("Please enter the second food item: "))
food2_price = float(input("Please enter the price for the second item: "))
food2_quantity = int(input("Please enter the number of second food you have: "))

food2_total = food2_price * food2_quantity

total_cost = food2_total + food1_total
gratuity = total_cost * .15

print("RECEIPT")
print(f"{food1_quantity} {food1} @ ${food1_price}0 = ${food1_total}0")
print(f"{food2_quantity} {food2} @ ${food2_price}0 = ${food2_total}0")
print(f"15% gratuity: ${gratuity}0 ")
print(f"Total cost: ${total_cost + gratuity}0")
