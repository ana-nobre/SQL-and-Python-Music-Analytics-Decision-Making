#%%
import os
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

#%%
def call(genre):
    results = []
    artist_list = []
    for offset in range(0,500,50):
        for year in range(2016,2021):
            datos = sp.search(q= f'genre:{genre}, year:{year}', type='track', limit=50, offset=offset) #offset se iguala para que cuando entre en el bucle for pueda iterar hasta extraer el número de tracks que queremos, es el límite por paginas y en spotify el máx es 50
            for item in datos['tracks']['items']: 
                release_date = item['album']['release_date']
                if release_date.startswith(str(year)): #la api de spotify no filtra el año en la query, #se necesita poner startswith para que en la fecha empieze por 2025 que es el año que queremos buscar
                    info = {   
                        'nombre_artista' : item['artists'][0]['name'],
                        'album' : item['album']['name'],
                        'fecha' : item['album']['release_date'],
                        'tipo' : item['type'],
                        'track' : item['name']
                    }

                    print("Este es el nombre del artista:", item['artists'][0]['name']), #nombre artista
                    print("Este es el nombre del album:",item['album']['name']), #nombre del album
                    print("Esta es la fecha de lanzamiento:", item['album']['release_date']), #fecha de lanzamiento
                    print("Este es el tipo de audio:", item['type']), #tipo 
                    print("Este es el nombre del track:", item['name']), #nom del track
                    print('..........')
                    
                    results.append(info)
                    artist_list.append(item['artists'][0]['name'])
    for artist in artist_list:
        print(artist)
    return results, artist_list

# %%
