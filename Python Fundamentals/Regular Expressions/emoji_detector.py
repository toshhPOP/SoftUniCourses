import re

command = input()
emoji_count = []
threshold = 1
emoji_pattern = r"(?P<sep>:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)"
digits_pattern = r"\d"
emojis = re.finditer(emoji_pattern, command)
for match in emojis:
    emoji_count.append(f"{match.group('sep')}{match.group('emoji')}{match.group('sep')}")
digits = re.finditer(digits_pattern, command)
counter = len(emoji_count)
for el in digits:
    threshold *= int(el.group())
print(f"Cool threshold: {threshold}")
print(f"{counter} emojis found in the text. The cool ones are:")
for el in emoji_count:
    coolness = sum([ord(x) for x in el if x != ':' and x != '*'])
    if coolness >= threshold:
        print(el)
