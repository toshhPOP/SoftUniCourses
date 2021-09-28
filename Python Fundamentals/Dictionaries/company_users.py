company = {}
while True:
    command = input()
    if command == "End":
        break
    company_name, id = command.split(" -> ")
    if company_name not in company:
        company[company_name] = []
    if id not in company[company_name]:
        company[company_name].append(id)
for k, v in sorted(company.items()):
    print(f"{k}")
    for user in range(len(v)):
        print(f"-- {v[user]}")
