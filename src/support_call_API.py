#%%
import os
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
#%% Specify the path to your .env file
env_path = '/Users/ananobre/Adalab_Bootcamp/Projetos Pessoais para Git/SQL-and-Python-Music-Analytics-Decision-Making/api.env'
loaded = load_dotenv(dotenv_path=env_path)
print("Env loaded:", loaded, "| Using:", env_path)
#%%

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("CLIENT_ID or CLIENT_SECRET not found in environment variables. "
                     "Please check your api.env file and path.")

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

print("Successfully authenticated with Spotify!")

API_KEY_LASTFM = os.getenv('API_KEY_LASTFM') 

if not API_KEY_LASTFM:
    raise ValueError("API_KEY_LASTFM not found in environment variables. "
                     "Please check  your api.env file and path.")

#%% Deliverable = Tracks's list 

def get_tracks_and_artists(genre,start_year=2020, end_year=2025):
    track_list = []
    artist_list = []
    for offset in range(0,500,50):
        for year in range(start_year,end_year):
            datos = sp.search(q= f'genre:{genre}, year:{year}', type='track', limit=50, offset=offset) 
            for item in datos['tracks']['items']: 
                release_date = item['album']['release_date']
                if release_date.startswith(str(year)): 
                    info = {   
                        'artist' : item['artists'][0]['name'],
                        'album' : item['album']['name'],
                        'date' : item['album']['release_date'],
                        'type' : item['type'],
                        'track' : item['name']
                    }

                    print("This is the artist's name:", item['artists'][0]['name']), # artist
                    print("This is the album name:", item['album']['name']), #album
                    print("This is the release date:", item['album']['release_date']), #date
                    print("This is the audio type:", item['type']), #type
                    print("This is the track name:", item['name']), #track
                    print('..........')

                    
                    track_list.append(info)
                    artist_list.append(item['artists'][0]['name'])
    return track_list, artist_list

# %% Deliverable = Albuns's list 
def get_album(genre, start_year=2020, end_year=2025):
    resultados_album = []

    for offset in range(0, 500, 50):  # hasta 500 resultados 
        datos = sp.search(q=f'{genre}', type='album', limit=50, offset=offset)

        for album in datos['albums']['items']:
            release_date = album.get('release_date', '')
            for year in range(start_year,end_year): 
                if release_date.startswith(str(year)):
                    info = {
                        'album': album['name'],
                        'date': release_date,
                        'type': album['album_type'],
                        'id': album['id']  
                    }
                    print("The album name is:", info['album'])
                    print("The release date is:", info['date'])
                    print("Type:", info['type'])
                    print("..........")
                    
                    resultados_album.append(info)
                    break

    return resultados_album

#%% Deliverable = Statistics from LastFM
def make_request_with_retries(url, params):
    for i in range(5):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200 and response.headers.get('content-length') != '0':
                return response
            else:
                print(f"Attempt {i+1} failed: status {response.status_code}, content-length {response.headers.get('content-length')}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i+1} failed with exception: {e}")
        time.sleep(1)
    return None

def get_statistics(artist):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': 'artist.getinfo',
        'artist' : artist,
        'api_key':  API_KEY_LASTFM,
        'format': 'json',
        'lang': 'es'
        }

    response = make_request_with_retries(url, params=params)
    if response:
        datos = response.json()
        if 'artist' in datos and 'stats' in datos['artist']:
            info = datos['artist']['stats'] 
            info_artist = {
                'artista': artist, 
                'listeners': info.get('listeners'),
                'playcount': info.get('playcount'),
                } 
            return info_artist
    print(f"Failed to get statistics for {artist} after multiple retries.")
    return None

def get_statistics_list(artist_list):
    statistics_list = []
    for artist in artist_list:
        print(f'getting statistics for {artist}')
        info = get_statistics(artist) # info_artist
        if info:
            statistics_list.append(info)
    return statistics_list

#%% Deliverable = Biographies 
def get_biographie(artist):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        
        'method': 'artist.getinfo',
        'artist' : artist,
        'api_key': API_KEY_LASTFM,
        'format': 'json',
        'lang': 'es'
        }
    
    response = make_request_with_retries(url, params=params)
    if response:
        datos = response.json()
        if 'artist' in datos and 'bio' in datos['artist'] and 'summary' in datos['artist']['bio']:
            info = datos['artist']['bio']['summary']
            info_biographie = {
                'artist': artist,
                'bio': info
                }
            return info_biographie
    print(f"Failed to get biography for {artist} after multiple retries.")
    return None
    
def get_biographies_list(unique_artist_list):
    biographies_list = []
    for artist in unique_artist_list:
        print(f'getting biographies for {artist}')
        info = get_biographie(artist)               # info_artist
        if info:
            biographies_list.append(info)
    return biographies_list




   