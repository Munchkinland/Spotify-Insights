import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Obtener las credenciales de Spotify desde variables de entorno
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://localhost:8888/callback'

# Definir el alcance de los permisos solicitados
scope = 'user-library-read user-top-read playlist-read-private'

class SpotifyClient:
    def __init__(self):
        # Configurar la autenticación de Spotify utilizando OAuth
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def get_track_data(self, track_id):
        track = self.sp.track(track_id)
        return {
            "track_id": track['id'],
            "track_name": track['name'],
            "artist_name": track['artists'][0]['name'],
            "album_name": track['album']['name'],
            "popularity": track['popularity']
        }

    def get_artist_data(self, artist_id):
        artist = self.sp.artist(artist_id)
        return {
            "artist_id": artist['id'],
            "artist_name": artist['name'],
            "genres": artist['genres'],
            "popularity": artist['popularity']
        }

    def get_playlist_data(self, playlist_id):
        playlist = self.sp.playlist(playlist_id)
        return {
            "playlist_id": playlist['id'],
            "playlist_name": playlist['name'],
            "tracks": [
                {
                    "track_id": track['track']['id'],
                    "track_name": track['track']['name'],
                    "artist_name": track['track']['artists'][0]['name']
                }
                for track in playlist['tracks']['items']
            ]
        }

    def get_user_data(self):
        user = self.sp.current_user()
        return {
            "user_id": user['id'],
            "display_name": user['display_name'],
            "followers": user['followers']['total']
        }

    def get_user_top_tracks(self):
        top_tracks = self.sp.current_user_top_tracks(limit=10)
        return [
            {
                "track_id": track['id'],
                "track_name": track['name'],
                "artist_name": track['artists'][0]['name'],
                "album_name": track['album']['name'],
                "popularity": track['popularity']
            }
            for track in top_tracks['items']
        ]

    def get_user_top_artists(self):
        top_artists = self.sp.current_user_top_artists(limit=10)
        return [
            {
                "artist_id": artist['id'],
                "artist_name": artist['name'],
                "genres": artist['genres'],
                "popularity": artist['popularity']
            }
            for artist in top_artists['items']
        ]
