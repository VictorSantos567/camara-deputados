import pandas as pd
from dao import get_all_partys_current
from datetime import datetime

def transform_partys_dict_to_dataframe():
    party =  get_all_partys_current()
    data = party['dados']
    df = pd.DataFrame(data)
    df = df.drop(['uri'], axis=1)
    return df

def current_date():
    today = str(datetime.now().date())
    return today



