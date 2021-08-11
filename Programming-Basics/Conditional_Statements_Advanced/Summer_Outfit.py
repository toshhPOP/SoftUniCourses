grad = int(input())
time_of_day = input()
if time_of_day == "Morning":
    if 10 <= grad <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < grad <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif grad >= 25:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= grad <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < grad <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif grad >= 25:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
elif time_of_day == "Evening":
    if 10 <= grad <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < grad <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif grad >= 25:
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f"It's {grad} degrees, get your {Outfit} and {Shoes}.")