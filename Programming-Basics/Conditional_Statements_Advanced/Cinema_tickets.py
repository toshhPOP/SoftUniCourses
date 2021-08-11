day = input()
ticket_price = 0
if day in ("Monday, Tuesday, Friday"):
    ticket_price = 12
elif day == "Wednesday" or day == "Thursday":
    ticket_price = 14
elif day == "Sunday" or day == "Saturday":
    ticket_price = 16
print(ticket_price)