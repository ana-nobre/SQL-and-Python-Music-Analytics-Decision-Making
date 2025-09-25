#%%
from src import support_call_api as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'pop', 'classical']
for genre in genre_list:
    resultados, artist_list = ap.get_tracks(genre)
    dm.load_track(resultados, genre)

genre_list = ['rock', 'jazz', 'pop', 'classical']
for genre in genre_list:
    resultados_album = ap.get_album(genre)
    dm.load_album(resultados_album, genre)

genre_list = ['rock', 'jazz', 'pop', 'classical']
for genre in genre_list:
    resultados_album = ap.get_biography(genre)
    dm.load_biography(resultados_album, genre)

genre_list = ['rock', 'jazz', 'pop', 'classical']
for genre in genre_list:
    resultados_album = ap.get_statistics(genre)
    dm.load_statistics(resultados_album, genre)