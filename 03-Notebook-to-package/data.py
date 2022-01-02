import pandas as pd


def get_data(nrows=10000):


    return  pd.read_csv("../01-Kaggle-Taxi-Fare/data/train.csv",nrows=nrows)

def clean_data(df, test=False):
    '''returns a DataFrame without outliers and missing values'''
    df=df[df.fare_amount > 0]
    df=df[df.distance < 100]
    df=df[df.passenger_count < 9]
    df=df[df.passenger_count > 0]
    # A COMPLETER
    return df