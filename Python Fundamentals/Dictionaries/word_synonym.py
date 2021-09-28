number = int(input())
synonyms = {}
for i in range(number):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word] += ", " + synonym
        continue
    synonyms[word] = synonym
for word in synonyms:
    print(f"{word} - {synonyms[word]}")
