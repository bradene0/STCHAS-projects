#Braden Evans
colors = {"red","blue","green","yellow","purple","orange","black","white","pink","brown","gray","grey","teal","maroon","navy","gold","silver"}
holidays = {"christmas","hanukkah","diwali","ramadan","easter","thanksgiving","new year","new-year","halloween","valentines","valentine's","labor day","labor-day","independence day","independence-day","mlk day","mlk-day","memorial day","memorial-day","veterans day","veterans-day","st patrick's day","st patricks day","st-patricks-day","passover"}

while True:
    a = input("1. Letter: ").strip()
    if len(a) == 1 and a.isalpha():
        a = a.upper()
        break
