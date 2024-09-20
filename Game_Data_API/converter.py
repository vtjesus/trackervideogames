# █▀▀ █▀█ █▄░█ █░█ █▀▀ █▀█ ▀█▀ █▀▀ █▀█
# █▄▄ █▄█ █░▀█ ▀▄▀ ██▄ █▀▄ ░█░ ██▄ █▀▄
# Script to convert and add more data to old json data using IGDB API
# INPUT: [{ "id": Int, "name": String, "year": Int, "img": String }]
# OUTPUT: [{ "id": Int, "name": String, "year": Int, "developer": String,
# "description": String, "website": String, "game_engines": List,
# "player_modes": List, "platforms": List, "pov": List, "genres": List,
# "themes": List, "keywords": List, "img": String, "rating": Float }]

import json
from IGDB import fetch_game_details
from main import download_cover_image

def get_json_data(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    processed_data = []
    for game in data:
        entry = {
            "game_id": game.get("id", ""),
            "game_name": game.get("name", ""),
            "game_image": game.get("img", ""),
            "game_year": game.get("year", ""),
        }
        processed_data.append(entry)
    return processed_data


game_data = get_json_data("test.json")
new_json = []

# Process each game entry
for i, game in enumerate(game_data):
    game_id = game["game_id"]
    name = game["game_name"]
    img = game["game_image"]
    year = game["game_year"]
    print(f"\nCURRENT GAME: {name} ({year})\n")

    game_details = fetch_game_details(name)
    (
        name,
        year,
        developer,
        description,
        cover,
        rating,
        genres,
        themes,
        keywords,
        website,
        engines,
        modes,
        platforms,
        povs,
    ) = game_details

    # Only process valid game details
    if name:
        new_json.append(
            {
                "id": game_id,
                "name": name,
                "year": year,
                "developer": developer,
                "description": description,
                "website": website,
                "game_engines": engines,
                "player_modes": modes,
                "platforms": platforms,
                "pov": povs,
                "genres": genres,
                "themes": themes,
                "keywords": keywords,
                "img": img,
                "rating": rating,
            }
        )
        # Download the cover image
        download_cover_image(cover, img)

    # Safety measure to limit processing to n entries
    # if i >= 3:
    #     break

# Save the new JSON data
with open("processed_games.json", "w") as outfile:
    json.dump(new_json, outfile, indent=4)

print("New JSON file 'processed_games.json' created successfully.")
