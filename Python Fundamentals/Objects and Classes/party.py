class Party():
    def __init__(self):
        self.people = []

guest_list = Party()

while True:
    command = input()
    if command == "End":
        break
    guest_list.people.append(command)
print(f"Going: {', '.join(guest_list.people)}\nTotal: {len(guest_list.people)}")