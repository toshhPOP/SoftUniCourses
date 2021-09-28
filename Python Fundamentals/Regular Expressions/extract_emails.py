import re

text = input()
pattern = r"\b(?P<mail>[A-Za-z0-9\.\-\_]+\@[A-Za-z\-]+\.[A-Z-a-z\.]+)\b"
email = re.finditer(pattern,text )
for e in email:
    print(e.group())