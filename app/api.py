from flask import Flask, jsonify, request
from spotify_client import SpotifyClient

app = Flask(__name__)
spotify_client = SpotifyClient()

@app.route('/spotify/track/<track_id>', methods=['GET'])
def get_track(track_id):
    track_data = spotify_client.get_track_data(track_id)
    return jsonify(track_data)

@app.route('/spotify/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist_data = spotify_client.get_artist_data(artist_id)
    return jsonify(artist_data)

@app.route('/spotify/playlist/<playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist_data = spotify_client.get_playlist_data(playlist_id)
    return jsonify(playlist_data)

@app.route('/spotify/user', methods=['GET'])
def get_user():
    user_data = spotify_client.get_user_data()
    return jsonify(user_data)

@app.route('/spotify/user/top/tracks', methods=['GET'])
def get_user_top_tracks():
    top_tracks = spotify_client.get_user_top_tracks()
    return jsonify(top_tracks)

@app.route('/spotify/user/top/artists', methods=['GET'])
def get_user_top_artists():
    top_artists = spotify_client.get_user_top_artists()
    return jsonify(top_artists)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
