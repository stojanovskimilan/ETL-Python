import pandas as pd
import numpy as np

def extract_data():
    return pd.read_excel('data\SpaceNK_2.0 (1).xlsx')

def transform_data(df):
    df = pd.read_excel('data\SpaceNK_2.0 (1).xlsx')
    df = df.dropna(how='all')
    df = df.tail(-1)

    column_names = df.iloc[0].values
    df.columns = column_names

    df = df.iloc[1:-1]

    df.drop(df.iloc[:, 0:2], inplace=True, axis=1)
    df = df.iloc[:,1:]
    df.drop(df.columns[[2]], axis=1, inplace=True)
    df = df.reset_index(drop=True)
    return df

if __name__ == '__main__':
    data = extract_data()
    transformed_data = transform_data(data)
    print(transformed_data)