banned_word = input().split(", ")
text = input()
for word in banned_word:
    text = text.replace(word, str(len(word) * "*"))
print(text)
