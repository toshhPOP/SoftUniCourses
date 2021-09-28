countries = input().split(", ")
capitals = input().split(", ")
capital_dictionary = {a: b for a, b in zip(countries, capitals)}
for country, capital in capital_dictionary.items():
    print(f"{country} -> {capital}")
