import json

with open('pokemons.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

keys_to_keep = [
    "Type",
    "EV Yield",
    "HP Base",
    "Attack Base",
    "Defense Base",
    "Special Attack Base",
    "Special Defense Base",
    "Speed Base"
]

filtered_data = {}

for pokemon, attributes in data.items():
    filtered_entry = {}
    for key in keys_to_keep:
        if key in attributes:
            value = attributes[key]
            try:
                filtered_entry[key] = int(value)
            except ValueError:
                filtered_entry[key] = value
    filtered_data[pokemon] = filtered_entry

with open('filtered_pokemons.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4, ensure_ascii=False)

print("Novi filtrirani JSON spremljen kao 'filtered_pokemons.json'")
