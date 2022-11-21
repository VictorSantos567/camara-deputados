import pandas as pd
from dao import get_all_partys_current

def transform_partys_dict_to_dataframe():
    party =  get_all_partys_current()
    data = party['dados']
    df = pd.DataFrame(data)
    return df
