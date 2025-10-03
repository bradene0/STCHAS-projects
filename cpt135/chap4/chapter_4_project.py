# Braden Evans
TICKET_PRICE = 10.00
SENIOR_DISCOUNT = .10
STUDENT_DISCOUNT = .20

def get_ticket_count():
    print("Welcome to Braden's Movie Theatre!")
    while True:
        raw = input("Tickets are 10$ each, please enter how many you would like(1-99): ").strip()
        if raw.isdigit():
            n = int(raw)
            if 1 <=n <=99:
                return n 

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y","n"):
            return ans == "y"

tickets = get_ticket_count()
print(f"You are purchasing {tickets} tickets.")
print("\nPlease enter the following information")
is_senior = get_yes_no("Are you over the age of 65? Y/N: ")
is_student = get_yes_no("Are you currently a student? Y/N: ")

subtotal = round(tickets * TICKET_PRICE, 2)
eligible_discounts = []
if is_student:
    eligible_discounts.append(("Student", STUDENT_DISCOUNT))
if is_senior:
    eligible_discounts.append(("Senior", SENIOR_DISCOUNT))

if eligible_discounts:
    discount_name, discount_rate = max(eligible_discounts, key=lambda x: x[1]) # my favorite concise selector(max by rate)
    discount_amount = round(subtotal * discount_rate, 2)
else:
    discount_name, discount_rate, discount_amount = None, 0.0, 0.0 # set defaults

total = round(subtotal - discount_amount, 2)

print("\n----------\n")
print("Braden's Movie Theatre Receipt\n")
print(f"{tickets} tickets @ $10: ${subtotal:.2f}")
if discount_amount > 0:
    pct = int(round(discount_rate * 100))
    print(f"{discount_name} discount ({pct}%): -${discount_amount:.2f}")
else:
    print("No eligible discounts: $0.00")
print(f"\nTotal: ${total:.2f}")
