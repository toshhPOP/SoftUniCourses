text = input()
result = text[0] +"".join([text[a] for a in range(1,len(text)) if text[a] != text[a-1]])
print(result)