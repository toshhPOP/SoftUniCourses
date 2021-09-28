tickets = [t.strip() for t in input().split(", ") if not t.isspace()]
winning_symbols = "@,#,$,^"
counter = 0
for ticket in tickets:
    match = False
    if len(ticket) < 20:
        print('invalid ticket')
        continue
    half = len(ticket) // 2
    left = ticket[:half]
    right = ticket[half:]
    for symbol in winning_symbols:
        if 6 <= left.count(symbol) <= 9 and 6 <= right.count(symbol) <= 9:
            print(f'ticket "{ticket}" - {left.count(symbol)}{symbol}')
            match = True
        elif left.count(symbol) == 10 and right.count(symbol) == 10:
            print(f'ticket "{ticket}" - {left.count(symbol)}{symbol} Jackpot!')
            match = True
    if match == False:
        print(f'ticket "{ticket}" - no match')
