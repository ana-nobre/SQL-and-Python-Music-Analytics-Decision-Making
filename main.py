#%%
from src import support_call_api as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'pop', 'classical']

for genre in genre_list:
    track_list, artist_list = ap.get_tracks_and_artists(genre, start_year=2024, end_year=2025)
    dm.load_track(track_list, genre)

    album_list = ap.get_album(genre, start_year=2024, end_year=2025)
    dm.load_album(album_list, genre)
    unique_artist_list = list(set(artist_list)) # derivable: unique artists

    statistics_list = ap.get_statistics_list(unique_artist_list)
    dm.load_statistics(statistics_list, genre)

    resultados_album = ap.get_biography(genre)
    dm.load_biography(resultados_album, genre)

# %%
