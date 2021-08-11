budget = float(input())
season = input()
expenses = 0
sleep = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = 0.3 * budget
        sleep = "Camp"
    elif season == "winter":
        expenses = 0.7 * budget
        sleep = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = 0.4 * budget
        sleep = "Camp"
    elif season == "winter":
        expenses = 0.8 * budget
        sleep = "Hotel"
elif budget > 1000:
    destination = "Europe"
    expenses = 0.9 * budget
    sleep = "Hotel"
print(f"Somewhere in {destination}")
print(f"{sleep} - {expenses:.2f}")
