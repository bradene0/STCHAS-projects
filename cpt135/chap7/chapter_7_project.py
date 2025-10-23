#Braden Evans
colors = {"red","blue","green","yellow","purple","orange","black","white","pink","brown","gray","grey","teal","maroon","navy","gold","silver"}
holidays = {"christmas","hanukkah","diwali","ramadan","easter","thanksgiving","new year","new-year","halloween","valentines","valentine's","labor day","labor-day","independence day","independence-day","mlk day","mlk-day","memorial day","memorial-day","veterans day","veterans-day","st patrick's day","st patricks day","st-patricks-day","passover"}

while True:
    a = input("1. Letter: ").strip()
    if len(a) == 1 and a.isalpha():
        a = a.upper()
        break

while True:
    v = input("2. Verb (past tense): ").strip().lower()
    if v.endswith("d"):
        break

while True:
    n = input("3. Noun (plural): ").strip().lower()
    if n.endswith("s"):
        break

while True:
    c = input("4. Color: ").strip().lower()
    if c in colors:
        break

while True:
    h_in = input("5. Holiday: ").strip().lower()
    if h_in in holidays:
        h = h_in.title()
        break

while True:
    p_in = input("6. Palindrome: ").strip()
    if p_in and p_in.casefold() == p_in.casefold()[::-1]:
        p = p_in.upper()
        break

print(f'A spy, Agent {a}, {v} into the abandoned {n} and looked for a key. All they found was a note that said, "I\'ll be wearing a {c} shirt at the {h} party." Remember the passcode "{p}".')
