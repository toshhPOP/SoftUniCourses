def collect_material(key_materials_dict: dict, junk_materials: dict, material: str, qty: int):
    if material == 'shards' or material == "fragments" or material == 'motes':
        key_materials_dict[material] += qty
    else:
        if material not in junk_materials.keys():
            junk_materials[material] = qty
        else:
            junk_materials[material] += qty


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
items_obtained = ""

while items_obtained == '':
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        material_quantity = int(current_line[i])
        material_name = current_line[i + 1].lower()

        collect_material(key_materials, junk, material_name, material_quantity)

        if key_materials["shards"] >= 250:
            items_obtained = "Shadowmourne"
            key_materials["shards"] -= 250
            break
        elif key_materials["fragments"] >= 250:
            items_obtained = "Valanyr"
            key_materials["fragments"] -= 250
            break
        elif key_materials["motes"] >= 250:
            items_obtained = "Dragonwrath"
            key_materials["motes"] -= 250
            break

sorted_dict = sorted(key_materials.items(),key=lambda kvp: (-kvp[1],kvp[0]))
print(f'{items_obtained} obtained!')
for key, value in sorted_dict:
    print(f"{key}: {value}")
for junk, qty in sorted(junk.items(),key=lambda kvp: kvp[0]):
    print(f"{junk}: {qty}")