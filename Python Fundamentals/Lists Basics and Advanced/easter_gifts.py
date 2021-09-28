gifts = input().split()
while True:
    text = input()
    if text == "No Money":
        break
    else:
        new = text.split()
        command = new[0]
        gift = new[1]
        if command == "OutOfStock":
            gifts = ["None" if x == gift else x for x in gifts]
        elif command == "Required":
            index = int(new[2])
            if index < len(gifts):
                gifts.pop(index)
                gifts.insert(index, gift)
        elif command == "JustInCase":
            gifts.pop()
            gifts.append(gift)

gifts = [x for x in gifts if x != "None"]
print(" ".join(gifts))