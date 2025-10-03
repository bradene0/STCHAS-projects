# Braden Evans
TICKET_PRICE = 10.00
SENIOR_DISCOUNT = .10
STUDENT_DISCOUNT = .20

def get_ticket_count():
    print("Welcome to my Movie Theatre!")
    while True:
        raw = input("Tickets are 10$ each, please enter how many you would like: ").strip()
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


