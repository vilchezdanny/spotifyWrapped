import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

TOP_SCOPE = "user-top-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=TOP_SCOPE))
results = sp.current_user_top_tracks(limit=100, time_range="long_term")
tracks = results["items"]

while results["next"]:
    results = sp.next(results)
    tracks.extend(results["items"])


top_tracks = []
for track in tracks:
    track_name = track["name"]
    artist_name = track["artists"][0]["name"]
    release_date = track["album"]["release_date"]
    duration = track["duration_ms"]
    song_popularity = track["popularity"]
    album_name = track["album"]["name"]
    album_img = track["album"]["images"][0]["url"]
    track_uri = track["uri"]
    artist_uri = track["artists"][0]["uri"]
    album_uri = track["album"]["uri"]

    top_tracks.append(
        [
            track_name,
            artist_name,
            release_date,
            duration,
            song_popularity,
            album_name,
            album_img,
            track_uri,
            artist_uri,
            album_uri,
        ]
    )

columns = [
    "track_name",
    "artist_name",
    "release_date",
    "duration",
    "song_popularity",
    "album_name",
    "album_img",
    "track_uri",
    "artist_uri",
    "album_uri",
]

top_tracks_df = pd.DataFrame(top_tracks, columns=columns)
top_tracks_df.to_csv("top_tracks.csv")
