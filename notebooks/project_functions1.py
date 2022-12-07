import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
from datetime import datetime

def load_and_process(url_or_path_to_csv_file):
    df1 = pd.read_csv(url_or_path_to_csv_file).dropna(axis = 0, inplace = True)
    
    df2 = {
        df1
        .drop(['is_geocoding_exact']==False, axis=1)
        .drop(['id', 'name', 'manner_of_death','city','signs_of_mental_illness','is_geocoding_exact', 'body_camera'], axis=1)
        .rename(columns={"date": "Date","armed":"Armed","age":"Age","gender":"Gender","race":"Race","state": "State","threat_level":"ThreatLevel","flee":"Flee","longitude":"Longitude","latitude":"Latitude"}, inplace = True)
       
      
        }
    return df2

   