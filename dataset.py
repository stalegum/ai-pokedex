import os
import pandas as pd
import requests

# Load your CSV with sprite URLs
df = pd.read_csv("data/gen5_pokemon_151_full_alphabetized.csv")

# Create base folder
base_dir = "dataset"
os.makedirs(base_dir, exist_ok=True)

for _, row in df.iterrows():
    name = row["name"].lower()
    folder_path = os.path.join(base_dir, name)
    os.makedirs(folder_path, exist_ok=True)

    # Download regular sprite
    if row["sprite_regular"]:
        try:
            r = requests.get(row["sprite_regular"])
            with open(os.path.join(folder_path, "regular.png"), "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Error downloading regular sprite for {name}: {e}")

    # Download shiny sprite
    if row["sprite_shiny"]:
        try:
            r = requests.get(row["sprite_shiny"])
            with open(os.path.join(folder_path, "shiny.png"), "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Error downloading shiny sprite for {name}: {e}")

print("✅ All folders and sprites created!")
