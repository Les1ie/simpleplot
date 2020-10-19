import csv
import pandas as pd
import numpy as np


class DataLoaderOption():
    '''
    '''
    pass


class DataLoader():

    opt = DataLoaderOption()

    def __init__(self, file_name: str) -> None:
        assert file_name.split(".")[-1].strip() == "csv",\
            "Only support csv file in current version."

        self.data = pd.read_csv(file_name,)

        self.data = self.data.astype(str)
        self.data = self.data.where(self.data != 'nan', None)

        # print(self.data.dtypes)
        # print(self.data)

    def tolist(self) -> list:
        return self.data.values.tolist()

    def get(self) -> pd.DataFrame:
        return self.data


def load_file(file_name, attributes)->pd.DataFrame:
  
    loader = DataLoader(file_name)
    df = loader.get()
    fill(df, attributes)
    return df

def fill(df: pd.DataFrame, attributes):
    for a in attributes:
        if a[0] not in df.columns:
            df.insert(len(df.columns), a[0], a[1])