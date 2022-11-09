import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(rawdata):

    df1 = (
         
          .rename(columns = {'armed': 'armed/unarmed'})
          .dropna('id','longitude','latitude','is_geocoding_exact', axis =1)
          .rename(columns={'armed': 'armed/unarmed'} 
               )
        
             
    
)
    return df2

   