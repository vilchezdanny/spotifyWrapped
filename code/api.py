#%%
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#%%
TOP_SCOPE = "user-top-read"
LIBRARY_SCOPE = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=TOP_SCOPE))

#%%
results = sp.current_user_top_tracks(limit=100, time_range="long_term")
# for idx, item in enumerate(results["items"]):
#     track = item["track"]
#     print(idx, track["artists"][0]["name"], " – ", track["name"])

# %%
print(results.keys())

# %%

print(results["items"][0].keys())

# %%
print(results["items"][0]["name"])


# %%
print(results["items"][0]["track"].keys())

# %%
print(results["items"][0]["track"]["artists"][0].keys())
# %%
