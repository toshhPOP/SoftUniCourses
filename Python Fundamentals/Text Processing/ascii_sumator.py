chr_1 = input()
chr_2 = input()
text = input()
result = [ord(text[x]) for x in range(len(text)) if ord(text[x]) in range(ord(chr_1)+1, ord(chr_2))]
print(sum(result))
