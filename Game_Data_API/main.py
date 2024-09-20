import os
import json
import requests
from IGDB import fetch_game_details


def main():
    game = input(str("Enter Name of the Game: "))

    game_details = fetch_game_details(game)
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

    # IF NOTHING
    if name == "":
        exit(0)

    img = input(str("Enter cover image filename: "))

    game_details = {
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

    game_json = json.dumps(game_details, indent=2)
    print(game_json)
    download_cover_image(cover, img)


def download_cover_image(hash, file_name):
    dir_path = "cover"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # Doc: https://api-docs.igdb.com/#images
    cover_size = "cover_big"  # 264 x 374
    if hash != "N/A":
        # //images.igdb.com/igdb/image/upload/t_thumb/xxxxxx.jpg
        url = f"https://images.igdb.com/igdb/image/upload/t_{cover_size}/{hash}.jpg"
        try:
            # COVER IMAGE
            response = requests.get(url)
            response.raise_for_status()
            with open(f"{dir_path}/{file_name}.jpg", "wb") as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Failed to download cover image: {e}")
    else:
        print("No valid cover URL provided.")


if __name__ == "__main__":
    main()
