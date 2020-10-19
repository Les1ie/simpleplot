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


def csv_to_list(file_name: str):
    dl = DataLoader(file_name=file_name)

    return dl.tolist()
