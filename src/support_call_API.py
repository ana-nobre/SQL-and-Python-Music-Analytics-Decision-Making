#%%
import os
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd
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
                        'nombre_artista' : item['artists'][0]['name'],
                        'album' : item['album']['name'],
                        'fecha' : item['album']['release_date'],
                        'tipo' : item['type'],
                        'track' : item['name']
                    }

                    print("Este es el nombre del artista:", item['artists'][0]['name']), # artist
                    print("Este es el nombre del album:",item['album']['name']), #album
                    print("Esta es la fecha de lanzamiento:", item['album']['release_date']), #date
                    print("Este es el tipo de audio:", item['type']), #type
                    print("Este es el nombre del track:", item['name']), #track
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
                        'fecha': release_date,
                        'tipo': album['album_type'],
                        'id': album['id']  
                    }
                    print("El nombre del álbum es:", info['album'])
                    print("La fecha de lanzamiento es:", info['fecha'])
                    print("Tipo:", info['tipo'])
                    print("..........")
                    
                    resultados_album.append(info)
                    break

    return resultados_album

#%% Deliverable = Statistics from LastFM
def get_statistics(artist):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': 'artist.getinfo',
        'artist' : artist,
        'api_key':  API_KEY_LASTFM,
        'format': 'json',
        'lang': 'es'
        }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Da error")
    else:
        datos = response.json()
        info = datos['artist']['stats'] 
        info_artist = {
            'artista': artist, 
            'oyentes': info.get('listeners'),
            'reproducciones': info.get('playcount'),
            } 
        return info_artist

def get_statistics_list(artist_list):
    statistics_list = []
    for artist in artist_list:
        print(f'getting statistics for {artist}')
        info = get_statistics(artist) # info_artist
        statistics_list.append(info)
    return statistics_list

#%% Deliverable = Biographies (WIP - see TODO.md)
def biographie(artist, api_key):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        
        'method': 'artist.getinfo',
        'artist' : artist,
        'api_key': api_key,
        'format': 'json'
        }
    biografias = []
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Da error")
    else:
        datos = response.json()
        resumen = datos['artist']['bio']['summary']
        return resumen