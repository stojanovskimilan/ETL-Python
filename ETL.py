import pandas as pd
import numpy as np
import psycopg2
from connect import *
from create_table import *
from insert_data import *
from drop_table import *

conn = psycopg2.connect(host="localhost",database="postgres",user="postgres",password="12345678")
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
    # connect()
    name = "Last_Week_Report_by_Store"
    # create_table(name) 
    # print("Created table: "+name)
    # drop_table(name)
    execute_values(conn=conn, df=transformed_data,table=name)


    