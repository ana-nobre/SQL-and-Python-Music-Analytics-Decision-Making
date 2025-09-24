#%%
from src import support_call_API as ap
from src import data_manipulation as dm

genre_list = ['rock', 'jazz', 'Pop']
for genre in genre_list:
    resultados, artist_list = ap.call(genre)
    dm.extract_artist(resultados, genre)


# %%
