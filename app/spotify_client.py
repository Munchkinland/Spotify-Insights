import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = os.getenv('SPOTIFY_CLIENT_ID', '2be385588dea41f6a5212617b87e7c30')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', 'a65e86032bef41cdac66b3136176237b')
redirect_uri = 'http://localhost:8888/callback'

scope = 'user-library-read user-top-read playlist-read-private'

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def get_track_data(self, track_id):
        return self.sp.track(track_id)

    def get_artist_data(self, artist_id):
        return self.sp.artist(artist_id)

    def get_playlist_data(self, playlist_id):
        return self.sp.playlist(playlist_id)

    def get_user_data(self):
        return self.sp.current_user()

    def get_user_top_tracks(self):
        return self.sp.current_user_top_tracks()

    def get_user_top_artists(self):
        return self.sp.current_user_top_artists()
