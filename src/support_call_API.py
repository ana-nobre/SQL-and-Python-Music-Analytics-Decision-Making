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

#%%

def get_biography(artist, api_key):
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
        
resultados, artist_list = get()
artistas_unic = pd.Series(artist_list)
artistas_unique = artistas_unic.unique()
print(artistas_unique)


resultados_nombres = []
limit = 200
contador = 0
for i in lista_artistas:
    if contador >= limit:
        break
    resumen = bio(i, api_key)
    resultados_nombres.append({
        'artista': i,
        'biografia': resumen
    })

    contador += 1

lista_artistas_limpia = [artista[0] if isinstance(artista, list) else artista for artista in lista_artistas] # clean brackets
df['artista'] = df['artista'].apply(lambda x: x[0] if isinstance(x, list) else x)

df_artist_jazz = pd.DataFrame(artistas_unic)
df_artist_jazz.to_csv('jazz_artists.csv', index=False)

df_artist_rock = pd.DataFrame(artist_list)
df_artist_rock.to_csv('pop_artists.csv', index=False)

df_artist_rock = pd.DataFrame(artist_list)
df_artist_rock.to_csv('rock_artists.csv', index=False)
df.to_csv('bio_rock.csv', index=False)

 """