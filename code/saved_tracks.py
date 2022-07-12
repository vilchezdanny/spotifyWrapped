import time
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth

LIBRARY_SCOPE = "user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=LIBRARY_SCOPE))
results = sp.current_user_saved_tracks(limit=50)
tracks = results["items"]

loop = 1
while results["next"]:
    print("Loop: {}".format(loop))
    loop += 1
    results = sp.next(results)
    tracks.extend(results["items"])
    # time.sleep(5)


saved_tracks = []s
for track in tracks:
    track_name = track["track"]["name"]
    artist_name = track["track"]["artists"][0]["name"]
    album_name = track["track"]["album"]["name"]
    release_date = track["track"]["album"]["release_date"]
    duration = track["track"]["duration_ms"]
    song_popularity = track["track"]["popularity"]
    album_img = track["track"]["album"]["images"][0]["url"]
    track_uri = track["track"]["uri"]
    artist_uri = track["track"]["artists"][0]["uri"]
    album_uri = track["track"]["album"]["uri"]

    saved_tracks.append(
        [
            track_name,
            artist_name,
            album_name,
            release_date,
            duration,
            song_popularity,
            album_img,
            track_uri,
            artist_uri,
            album_uri,
        ]
    )

columns = [
    "track_name",
    "artist_name",
    "album_name",
    "release_date",
    "duration",
    "song_popularity",
    "album_img",
    "track_uri",
    "artist_uri",
    "album_uri",
]

saved_tracks_df = pd.DataFrame(saved_tracks, columns=columns)
saved_tracks_df.to_csv("saved_tracks.csv", index=False)
