import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # take environment variables from .env.
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def check_if_authenticated():
    # AUTHENTICATING TWITCH APP (TO GET ACCESS_TOKEN)
    # POST REQUEST: https://id.twitch.tv/oauth2/token?client_id=abcdefg12345&client_secret=hijklmn67890&grant_type=client_credentials
    # RESPONSE: { "access_token": "access12345token", "expires_in": 5587808, "token_type": "bearer" }
    if ACCESS_TOKEN == "":
        response = requests.post(
            f"https://id.twitch.tv/oauth2/token?client_id={TWITCH_CLIENT_ID}&client_secret={TWITCH_CLIENT_SECRET}&grant_type=client_credentials"
        )
        print("RESPONSE: %s" % str(response.json()))
        exit(0)


def get_field_names(game, field):
    return [item.get("name", "N/A") for item in game.get(field, [])]


def get_first_field(game, field, key):
    return game.get(field, [{}])[0].get(key, "N/A")


def get_first_developer_company(game):
    companies = game.get("involved_companies", [])
    # [{'id':xxxxx, 'company': {'id': xxx, 'name': 'xxxxxxxxxxxxxx'}, 'developer': True}]
    if not isinstance(companies, list):
        return "N/A"
    for company_info in companies:
        if company_info.get("developer"):
            return company_info["company"].get("name", "N/A")
    return "N/A"


# UNIX TIMESTAMP TO ISO
def format_year(unix_timestamp):
    release_year = 0
    if unix_timestamp != "":
        release_year = datetime.fromtimestamp(int(unix_timestamp)).strftime("%Y")
        release_year = int(release_year)
        # .strftime('%Y-%m-%d %H:%M:%S'))
    return release_year


# DOUBLE TO 1 DECIMAL FLOAT
def format_rating(rating):
    try:
        rating = int(rating)
        rating = round(rating, 1)  # Round to 1 decimal
    except:
        rating = 0
    return rating


def format_game(game):
    nm = game.get("name", "")
    yr = format_year(game.get("first_release_date", ""))
    dev = get_first_developer_company(game)
    dc = game.get("summary", "")
    cr = game.get("cover", {}).get("image_id", "")
    rt = format_rating(game.get("rating", ""))
    gnr = get_field_names(game, "genres")
    thm = get_field_names(game, "themes")
    key = get_field_names(game, "keywords")
    web = get_first_field(game, "websites", "url")
    eng = get_field_names(game, "game_engines")
    mod = get_field_names(game, "game_modes")
    plt = get_field_names(game, "platforms")
    psp = get_field_names(game, "player_perspectives")
    return [nm, yr, dev, dc, cr, rt, gnr, thm, key, web, eng, mod, plt, psp]


def fetch_game_details(title):
    check_if_authenticated()

    # FETCHING IGDB GAME DATA (WITH ACCESS TOKEN)
    igdb_url = "https://api.igdb.com/v4/games"
    headers = {"Client-ID": TWITCH_CLIENT_ID, "Authorization": f"Bearer {ACCESS_TOKEN}"}
    body = f"""
    fields name, first_release_date, involved_companies.company.name,
    involved_companies.developer, summary, rating, cover.image_id, genres.name,
    themes.name, keywords.name, websites.url, game_engines.name,
    game_modes.name, platforms.name, player_perspectives.name; search
    "{title}"; limit 16;
    """

    response = requests.post(igdb_url, headers=headers, data=body)
    games = response.json()

    if games == []:
        print("Couldn't find the game")
        return ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    if response.status_code == 200:
        # GET RESPONSE
        game = response.json()[0] if response.json() else {}
        name = game.get("name", "")
        release_year = format_year(game.get("first_release_date", ""))

        # PRINT DATA
        name = game.get("name", "")
        release_year = format_year(game.get("first_release_date", ""))
        platforms = get_field_names(game, "platforms")
        print(f"[x] {name} ({release_year})")
        print(f"    {'|'.join(platforms)}")

        # READ CONFIRMATION AND RETURN DATA
        proceed = input(str("\nProceed? (Y/n): ")).lower()
        if proceed == "y" or proceed == "":
            return format_game(game)

        # SOMETHING WRONG?
        else:
            # PRINT OTHER CHOICES
            i = 1
            for game in games:
                name = game.get("name", "")
                release_year = format_year(game.get("first_release_date", ""))
                platforms = get_field_names(game, "platforms")
                print(f"[{i}] {name} ({release_year})")
                print(f"    {'|'.join(platforms)}")
                i += 1

            # READ USER SELECTION
            selected_game = len(games) + 1
            try:
                selected_game = int(input("\nSelect a game: "))
                while selected_game > len(games):
                    print("umm... That's not even in the list")
                    selected_game = int(input("Select a game: "))
            except:
                print("Looks like what you are looking for is not here")
                return ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

            # RETURN SELECTED DATA
            game = response.json()[selected_game - 1] if response.json() else {}
            return format_game(game)

    else:
        print(f"Request for {title} failed. Status: {response.status_code}")
        print("Looks like it's time to regenerate your ACCESS_TOKEN")
        return ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
