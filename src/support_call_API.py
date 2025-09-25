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

def get_tracks(genre):
    results = []
    artist_list = []
    for offset in range(0,500,50):
        for year in range(2016,2021):
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
                    
                    results.append(info)
                    artist_list.append(item['artists'][0]['name'])
    for artist in artist_list:
        print(artist)
    return results, artist_list

# %% Deliverable = Albuns's list 
def get_album(genre):
    resultados_album = []

    for offset in range(0, 500, 50):  # hasta 500 resultados (Spotify limita a 1000 máx)
        datos = sp.search(q=f'{genre}', type='album', limit=50, offset=offset)

        for album in datos['albums']['items']:
            release_date = album.get('release_date', '')
            for year in range(2016, 2021):  # años 2016 a 2020
                if release_date.startswith(str(year)):
                    info = {
                        'album': album['name'],
                        'fecha': release_date,
                        'tipo': album['album_type'],
                        'id': album['id']  # puedes eliminar esto si no lo necesitas
                    }
                    print("El nombre del álbum es:", info['album'])
                    print("La fecha de lanzamiento es:", info['fecha'])
                    print("Tipo:", info['tipo'])
                    print("..........")
                    
                    resultados_album.append(info)
                    break

    return resultados_album

#%% Deliverable = Statistics
def get_statistics(id_genero, artist, api_key):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': 'artist.getinfo',
        'artist' : artist,
        'api_key':  api_key,
        'format': 'json',
        'lang': 'es'
        }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Da error")
    else:
        datos = response.json()
        info = datos['artist']['stats'] #extraer listeners y plays por separado
        info_artista = {
            'id_genero': id_genero,
            'artista': artist, 
            'oyentes': info.get('listeners'),
            'reproducciones': info.get('playcount'),
            } 
        return info_artista
    
#%% Deliverable = Biographys
def bio(artist, api_key):
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