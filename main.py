#%%
from src import support_call_api as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'pop', 'classical']

for genre in genre_list:
    resultados, artist_list = ap.get_tracks(genre)
    dm.load_track(resultados, genre)

    resultados_album = ap.get_album(genre)
    dm.load_album(resultados_album, genre)

    resultados_album = ap.get_statistics(id_genero, artist_list, api_key)
    dm.load_statistics(resultados_album, genre)

    resultados_album = ap.get_biography(genre)
    dm.load_biography(resultados_album, genre)

#    stats(1,"Bach",api_key)