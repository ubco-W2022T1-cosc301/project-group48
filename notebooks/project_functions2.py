import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(data):
    
    df1 = (
        
        data["State"] == data["state"].replace(states)
        data["date"] = pd.to_datetime(data["date"])
        data["Year"] = data["date"].dt.year
        data["manner_of_death"].replace({"shot":"Shot", "shot and Tasered":"Shot and Tasered"}, inplace = True)
        data["armed"].replace({"gun":"Gun", "knife":"Knife", "unarmed":"Unarmed", "undetermined":"Undetermined", "vehicle":"Vehicle",
                               "toy weapon":"Toy Weapon", "unknown weapon":"Unknown Weapon", "machete":"Machete"}, inplace = True)
        data["gender"].replace({"M":"Male", "F":"Female"}, inplace = True)
        data["signs_of_mental_illness"].replace({True:"Abnormal", False:"Normal"}, inplace = True)
        data["body_camera"].replace({True:"Available", False:"Not Available"}, inplace = True)
        data["race"].replace({"W":"White", "B":"Black", "H":"Hispanic", "A":"Asian", "N":"Native", "O":"Other"}, inplace = True)
        data["threat_level"].replace({"attack":"Attack", "other":"Not Attack", "undetermined":"Unknown"}, inplace = True)
        data["flee"].replace({"Not fleeing":"Not Fleeing", "Other":"Unknown"}, inplace = True)
        data.rename(columns={"name": "Name","date": "Date","manner_of_death": "Manner OfDeath","armed":"Armed","age":"Age","gender":"Gender","race":"Race","city":"City","state": "StateCode","signs_of_mental_illness":"Mental Illness","threat_level":"Threat Level","flee":"Flee","body_camera":"Footage"}, inplace = True)
        data = data[["Year","City","State", "State Code","Name","Age","Gender","Race","Mental=Illness","Armed","Threat Level","Manner Of Death","Flee","Footage"]]


    return df1

   