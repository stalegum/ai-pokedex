print("🚀 Starting full Gen 1 dataset build...")

import os
import requests

gen1_names = sorted([
    "abra", "aerodactyl", "alakazam", "arbok", "arcanine", "articuno", "beedrill", "bellsprout",
    "blastoise", "bulbasaur", "butterfree", "caterpie", "chansey", "charizard", "charmander",
    "charmeleon", "clefable", "clefairy", "cloyster", "cubone", "dewgong", "diglett", "ditto",
    "dodrio", "doduo", "dragonair", "dragonite", "dratini", "drowzee", "dugtrio", "eevee",
    "ekans", "electabuzz", "electrode", "exeggcute", "exeggutor", "farfetchd", "fearow", "flareon",
    "gastly", "gengar", "geodude", "gloom", "golbat", "goldeen", "golduck", "golem", "graveler",
    "grimer", "growlithe", "gyarados", "haunter", "hitmonchan", "hitmonlee", "horsea", "hypno",
    "ivysaur", "jigglypuff", "jolteon", "jynx", "kabuto", "kabutops", "kadabra", "kakuna", "kangaskhan",
    "kingler", "koffing", "krabby", "lapras", "lickitung", "machamp", "machoke", "machop",
    "magikarp", "magmar", "magnemite", "magneton", "mankey", "marowak", "meowth", "metapod", "mew",
    "mewtwo", "moltres", "mr-mime", "muk", "nidoking", "nidoqueen", "nidoran-f", "nidoran-m",
    "nidorina", "nidorino", "ninetales", "oddish", "omanyte", "omastar", "onix", "paras", "parasect",
    "persian", "pidgeot", "pidgeotto", "pidgey", "pikachu", "pinsir", "poliwag", "poliwhirl",
    "poliwrath", "ponyta", "porygon", "primeape", "psyduck", "raichu", "rapidash", "raticate",
    "rattata", "rhydon", "rhyhorn", "sandshrew", "sandslash", "scyther", "seadra", "seaking",
    "seel", "shellder", "slowbro", "slowpoke", "snorlax", "spearow", "squirtle", "starmie",
    "staryu", "tangela", "tauros", "tentacool", "tentacruel", "vaporeon", "venomoth", "venonat",
    "venusaur", "victreebel", "vileplume", "voltorb", "vulpix", "wartortle", "weedle", "weepinbell",
    "weezing", "wigglytuff", "zapdos", "zubat"
])

base_url = "https://img.pokemondb.net/sprites/black-white"

def download_sprite(url, path):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"✅ {path}")
        else:
            print(f"❌ Not found: {url}")
    except Exception as e:
        print(f"⚠️ Error downloading {url}: {e}")

for name in gen1_names:
    folder = os.path.join("dataset", name)
    os.makedirs(folder, exist_ok=True)

    sprite_urls = {
        "front.png": f"{base_url}/normal/{name}.png",
        "shiny.png": f"{base_url}/shiny/{name}.png",
        "back.png": f"{base_url}/back-normal/{name}.png",
        "back_shiny.png": f"{base_url}/back-shiny/{name}.png"
    }

    for filename, url in sprite_urls.items():
        filepath = os.path.join(folder, filename)
        download_sprite(url, filepath)

    # Add placeholder for anime screenshots
    with open(os.path.join(folder, "anime_placeholder.txt"), "w") as f:
        f.write("Drop anime screenshots here.")