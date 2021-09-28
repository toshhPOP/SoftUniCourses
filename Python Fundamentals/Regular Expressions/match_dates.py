import re

pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})"
text = input()
dates = re.findall(pattern,text)
for match in dates:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")