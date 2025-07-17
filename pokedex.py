import pandas as pd

# Load the CSV file (ensure this matches your actual path)
data = pd.read_csv("data/gen1_pokemon_metadata.csv")

def get_pokemon_info(name):
    # Case-insensitive match
    result = data[data['name'].str.lower() == name.lower()]
    
    if result.empty:
        return {
            "name": "Not Found",
            "type": "N/A",
            "ability": "N/A",
            "bst": "N/A",
            "pokedex_description": "Not available.",
            "sprite_front": "",
            "sprite_back": "",
            "sprite_shiny": "",
            "sprite_back_shiny": ""
        }

    row = result.iloc[0]
    type_2 = row["type_2"] if pd.notna(row["type_2"]) else ""
    return {
        "name": row["name"],
        "type": f"{row['type_1']} {type_2}".strip(),
        "ability": row["ability"],
        "bst": str(row["bst"]),
        "pokedex_description": row["pokedex_description"],
        "sprite_front": row["sprite_front"],
        "sprite_back": row["sprite_back"],
        "sprite_shiny": row["sprite_shiny"],
        "sprite_back_shiny": row["sprite_back_shiny"]
    }

