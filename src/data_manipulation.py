#%%
import pandas as pd

def extract_artist(results, genre):
    df = pd.DataFrame(results)
    fileName = f'track_{genre}.csv'
    df.to_csv(fileName, index=False)