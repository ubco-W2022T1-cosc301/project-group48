import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url):
    df1 = pd.read_csv(url).dropna()
    
    df2 = (
        df1
        .rename(columns={'name':'Name','date':'Date'})
        .rename(columns={'manner_of_death': 'Manner of Death', 'armed':'Armed'})
        .drop(['id','longitude','latitude','is_geocoding_exact'], axis=1)
    )
    return df2

   