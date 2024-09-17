import os
import json
import time
import webbrowser
from threading import Thread
from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import configparser

config = configparser.ConfigParser()
config.read('cred.txt')

# Extract the credentials
SPOTIPY_CLIENT_ID = config.get('DEFAULT', 'SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = config.get('DEFAULT', 'SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = config.get('DEFAULT', 'SPOTIPY_REDIRECT_URI')

os.environ['SPOTIPY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URI'] = SPOTIPY_REDIRECT_URI

scope = 'user-modify-playback-state user-read-playback-state'
sp_oauth = SpotifyOAuth(scope=scope)

# Flask setup
app = Flask(__name__)

@app.route('/')
def index():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    with open('token_info.json', 'w') as f:
        json.dump(token_info, f)
    return "You can close this tab now. Authentication is complete."

def initialize_spotify():
    # Run Flask app in a separate thread
    flask_thread = Thread(target=lambda: app.run(port=8889))
    flask_thread.start()

def get_token():
    token_info = None
    try:
        with open('token_info.json', 'r') as f:
            token_info = json.load(f)
    except FileNotFoundError:
        pass

    if not token_info:
        webbrowser.open('http://localhost:8889')
        while not token_info:
            try:
                with open('token_info.json', 'r') as f:
                    token_info = json.load(f)
            except:
                pass
            time.sleep(1)

    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        with open('token_info.json', 'w') as f:
            json.dump(token_info, f)

    return token_info['access_token']

def play_song(track_uri):
    token = get_token()
    sp = spotipy.Spotify(auth=token)
    sp.start_playback(uris=[track_uri])

def pause_song():
    token = get_token()
    sp = spotipy.Spotify(auth=token)
    sp.pause_playback()

def resume_song():
    token = get_token()
    sp = spotipy.Spotify(auth=token)
    sp.start_playback()

def stop_song():
    pause_song()
