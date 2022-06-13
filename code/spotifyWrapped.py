import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


auth_manager = SpotifyOAuth(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["SECRET"],
    redirect_uri=os.environ["URL"],
)
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.artist_albums(os.environ["URL"], album_type="album")
albums = results["items"]
while results["next"]:
    results = sp.next(results)
    albums.extend(results["items"])

for album in albums:
    print(album["name"])
