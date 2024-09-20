# GAME DATA API

## 🚀 Quickstart

Step 1: Register an **Application** on [Twitch Developers Page](https://dev.twitch.tv/console)

Step 2: Get **TWITCH_CLIENT_ID** and Generate **TWITCH_CLIENT_SECRET** from your **Application**

Step 3: Add **.env** file and put both **TWITCH_CLIENT_ID** and **TWITCH_CLIENT_SECRET** in it like

```bash
TWITCH_CLIENT_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWITCH_CLIENT_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
ACCESS_TOKEN=""
```

Step 4: Run Python Script with

```bash
python main.py
```

Step 5: That's it! You now got your **ACCESS_TOKEN** which you can put in you .env file

📔 Note: If ACCESS_TOKEN is expired or lost, just clear the value in .env and run script again

For more details, refer [IGDB API Docs](https://api-docs.igdb.com/)

## Data Structure

```py
game_details = {
    "name": String,
    "release_year": Int,
    "developer": String,
    "description": String,
    "website": String,
    "game_engines": List,
    "player_modes": List,
    "platforms": List,
    "pov": List,
    "genres": List,
    "themes": List,
    "keywords": List,
    "img": String,
    "rating": Float,
}
```

## Note

- logos are available at steamgriddb
