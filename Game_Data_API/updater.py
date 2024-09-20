# █░█ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀ █▀█
# █▄█ █▀▀ █▄▀ █▀█ ░█░ ██▄ █▀▄
# Script to update or add more entries

import json


# CURRENT GAME DATA
def get_json_data(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    processed_data = []
    for game in data:
        entry = {
            "id": game.get("id", ""),
            "name": game.get("name", ""),
            "year": game.get("year", ""),
            "developer": game.get("developer", ""),
            "description": game.get("description", ""),
            "website": game.get("website", ""),
            "game_engines": game.get("game_engines", []),
            "player_modes": game.get("player_modes", []),
            "platforms": game.get("platforms", []),
            "pov": game.get("pov", []),
            "genres": game.get("genres", []),
            "themes": game.get("themes", []),
            "keywords": game.get("keywords", []),
            "img": game.get("img", ""),
            "rating": game.get("rating", ""),
        }
        processed_data.append(entry)
    return processed_data


game_data = get_json_data("games.json")
new_json = []

# INPUT STRUCTURE
for i, game in enumerate(game_data):
    id = game["id"]
    name = game["name"]
    year = game["year"]
    developer = game["developer"]
    description = game["description"]
    website = game["website"]
    game_engines = game["game_engines"]
    player_modes = game["player_modes"]
    platforms = game["platforms"]
    pov = game["pov"]
    genres = game["genres"]
    themes = game["themes"]
    keywords = game["keywords"]
    img = game["img"]
    rating = game["rating"]

    # OUTPUT STRUCTURE
    if name:
        new_json.append(
            {
                "id": id,
                "name": name,
                "year": year,
                "developer": developer,
                "description": description,
                "website": website,
                "game_engines": game_engines,
                "player_modes": player_modes,
                "platforms": platforms,
                "pov": pov,
                "genres": genres,
                "themes": themes,
                "keywords": keywords,
                "img": img,
                "playtime": 0,
                "rating": rating,
            }
        )

# Save the new JSON data
with open("games.json", "w") as outfile:
    json.dump(new_json, outfile, indent=4)

print("New JSON file 'games.json' created successfully.")
