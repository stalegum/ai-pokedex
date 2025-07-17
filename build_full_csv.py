import csv
import requests

def get_pokemon_data(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    species = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}").json()
    p = requests.get(url).json()

    name = p["name"]
    types = [t["type"]["name"] for t in p["types"]]
    ability = p["abilities"][0]["ability"]["name"]
    bst = sum(s["base_stat"] for s in p["stats"])
    desc = ""
    for entry in species["flavor_text_entries"]:
        if entry["language"]["name"] == "en" and entry["version"]["name"] in ["red", "blue", "yellow"]:
            desc = entry["flavor_text"].replace("\n", " ").replace("\x0c", " ")
            break

    base = "black-white"
    front = f"https://img.pokemondb.net/sprites/{base}/normal/{name}.png"
    shiny = front.replace("/normal/", "/shiny/")
    back = f"https://img.pokemondb.net/sprites/{base}/back-normal/{name}.png"
    back_shiny = back.replace("/back-normal/", "/back-shiny/")

    return {
        "name": name, "type_1": types[0], "type_2": types[1] if len(types) > 1 else "",
        "ability": ability, "bst": bst, "pokedex_description": desc,
        "sprite_front": front, "sprite_shiny": shiny,
        "sprite_back": back, "sprite_back_shiny": back_shiny
    }

# Create CSV
with open("gen1_full_metadata.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "name","type_1","type_2","ability","bst","pokedex_description",
        "sprite_front","sprite_shiny","sprite_back","sprite_back_shiny"
    ])
    writer.writeheader()
    for i in range(1, 152):
        row = get_pokemon_data(i)
        writer.writerow(row)
        print(f"✅ {row['name']} written")

print("🎉 All 151 Pokémon data generated into gen1_full_metadata.csv!")
