#%%
import pandas as pd

def load_track(results, genre):
    df = pd.DataFrame(results)
    fileName = f'track_{genre}.csv'
    df.to_csv(fileName, index=False)

def load_album(results, genre):
    df = pd.DataFrame(results)
    fileName = f'album_{genre}.csv'
    df.to_csv(fileName, index=False)

def load_biography(results, genre):
    df = pd.DataFrame(results)
    fileName = f'biography_{genre}.csv'
    df.to_csv(fileName, index=False)

def load_statistics(results, genre):
    df = pd.DataFrame(results)
    fileName = f'statistics_{genre}.csv'
    df.to_csv(fileName, index=False)


# %%
