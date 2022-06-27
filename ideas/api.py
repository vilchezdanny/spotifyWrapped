from enum import Enum
from spotipy.oauth2 import SpotifyOAuth
import spotipy


class ScopeType(Enum):
    TOP_SCOPE = "user-top-read"
    LIBRARY_SCOPE = "user-library-read"
    PLAYLIST_SCOPE = "playlist-read-private"


class APIConnection:
    def __init__(self, scope: ScopeType) -> None:
        self.scope = scope
        self.auth = SpotifyOAuth(scope=self.scope)
        self.connect = spotipy.Spotify(auth_manager=self.auth)

    def get_top_tracks(self, limit=50, time_range)
connection = APIConnection(ScopeType.TOP_SCOPE.value)
results = connection.connect.current_user_top_tracks(limit=5, time_range="long_term")
