import re

pattern = r"([\#|\@])(?P<worlds>[A-Za-z]{3,})(\1{2})([A-Za-z]{3,})"
text = input()
words = re.finditer(pattern, text)
wo_rd = [el.group().strip("#") if "#" in el.group() else el.group().strip("@") for el in words]
wo_rd = [a.replace("#", "") if "#" in a else a for a in wo_rd]
wo_rd = [a.replace("@", "") if "@" in a else a for a in wo_rd]
if len(wo_rd) == 0:
    print("No word pairs found!")
else:
    print(f"{len(wo_rd)} word pairs found!")
mirror_worlds = [a for a in wo_rd if a[:len(a) // 2:] == a[len(a) // 2:][::-1] or a[len(a) // 2:] == a[:len(a) // 2][::-1]]
mirror_worlds = [mirror_worlds[el][:int(len(mirror_worlds[el]) / 2)] + " <=> " + mirror_worlds[el][int(len(
    mirror_worlds[el]) / 2):] for el in range(len(mirror_worlds))]
if len(mirror_worlds) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_worlds))
else:
    print("No mirror words!")
