import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

TOP_SCOPE = "user-top-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=TOP_SCOPE))
results = sp.current_user_top_artists(limit=100, time_range="long_term")
artists = results["items"]

while results["next"]:
    results = sp.next(results)
    artists.extend(results["items"])


top_artists = []

for artist in artists:
    artist_name = artist["name"]
    genre = artist["genres"]
    artist_popularity = artist["popularity"]
    artist_uri = artist["uri"]
    artist_img = artist["images"][0]["url"]

    top_artists.append(
        [
            artist_name,
            genre,
            artist_popularity,
            artist_uri,
            artist_img,
        ]
    )

columns = [
    "artist_name",
    "genre",
    "artist_popularity",
    "artist_uri",
    "artist_img",
]

top_artists_df = pd.DataFrame(top_artists, columns=columns)
top_artists_df.to_csv("./data/top_artists.csv")
