gifts = input().split()
while True:
    command = input()
    if command != "No Money":
        word = command.split()
        gift = word[1]
        if "OutOfStock" in word:
            gifts = ["None" if x == gift else x for x in gifts]
        elif "Required" in word:
            index = int(word[2])
            if 0 <= index < len(gifts):
                gifts.pop(index)
                gifts.insert(index,gift)
        elif command == 'JustInCase':
            gifts.pop()
            gifts.append(gift)
    else:
        gifts = [x for x in gifts if x != "None"]
        print(" ".join(gifts))
        break